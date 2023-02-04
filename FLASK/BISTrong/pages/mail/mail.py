from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from utilities.db.db_manager import dbManager

# mail blueprint definition
mail = Blueprint('mail', __name__, static_folder='static', static_url_path='/mail', template_folder='templates')


# Routes
@mail.route('/mail', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    train = False
    currentMail = False
    if request.args.__contains__('DT'):
        if request.args.get('new') == '1':
            session['newMails'] = session['newMails'] - 1
        currentMail = {}
        DT = request.args.get('DT')
        query = "SELECT M.*, U.name FROM mails AS M JOIN user AS U on U.user_id = M.senderID WHERE DT = \"%s\" AND receiverID = %s" % (
        DT, session['userID'])
        currentMail = dbManager.fetch(query)
        train = False
        if currentMail[0].trainDT:
            query = "SELECT DL.day_name, DL.date FROM train AS T JOIN date_lookup AS DL on T.trainingDate = DL.date " \
                    "WHERE T.user_id = %s AND T.UploadDT = \"%s\"" % (session['userID'], currentMail[0].trainDT)
            train = dbManager.fetch(query)

        query = "UPDATE mails SET isNew = FALSE WHERE receiverID = %s AND DT = \"%s\"" % (session['userID'], DT)
        dbManager.commit(query)

    query = "SELECT M.receiverID, M.DT, M.headline, M.isNew, U.name, m.content  " \
            "FROM mails AS M " \
            "JOIN user AS U on U.user_id = M.senderID " \
            "WHERE M.receiverID = %s " \
            "ORDER BY M.DT DESC " % (session['userID'],)
    inbox = dbManager.fetch(query)
    query = "SELECT name FROM user"
    mailNames = dbManager.fetch(query)

    return render_template('mail.html', inbox=inbox, train=train, currentMail=currentMail, mailNames=mailNames)


@mail.route('/deleteMail', methods=['GET', 'POST'])
def deleteMail():
    sender = request.args.get('sender')
    DT = request.args.get('DT')
    query = "SELECT user_id FROM user WHERE name = \"%s\"" % (sender,)
    res = dbManager.fetch(query)
    if not res:
        flash('בעיה בשם השולח, המייל לא נמחק')
        return redirect('/mail')
    senderID = res[0].user_id
    query = "DELETE FROM mails WHERE DT = \"%s\" AND senderID = %s" % (DT, senderID)
    res = dbManager.commit(query)
    if res == -1:
        flash('המחיקה נכשלה, בבקשה נסה שוב')
        return redirect('/mail')
    flash('המייל נמחק בהצלחה!')
    return redirect('/mail')
