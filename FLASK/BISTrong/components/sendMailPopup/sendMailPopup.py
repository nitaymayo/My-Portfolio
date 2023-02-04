from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from datetime import datetime
from utilities.db.db_manager import dbManager
# sendMailPopup blueprint definition
sendMailPopup = Blueprint('sendMailPopup', __name__, static_folder='static', static_url_path='/sendMailPopup', template_folder='templates')


@sendMailPopup.route('/sendMail', methods=['GET', 'POST'])
def sendMail():
    sendTo = request.form.get('sendTo')
    sendTo = sendTo.strip()
    headline = request.form.get('headline')
    content = request.form.get('content')
    DT = datetime.now()
    query = "SELECT user_id FROM user WHERE name = \"%s\"" % (sendTo,)
    res = dbManager.fetch(query)
    if res:
        sendToID = res[0].user_id
    else:
        flash('בעיה בשם הנמען, מייל לא נשלח בבקשה נסה שוב')
        return redirect(url_for('mail.index'))
    if request.form.__contains__('trainUploadDTInput'):
        mailTrainUploadDT = request.form.get('trainUploadDTInput')
        query = "INSERT INTO mails(SENDERID, DT, RECEIVERID, TRAINID, TRAINDT, HEADLINE, CONTENT) " \
                "VALUES (%s, \"%s\", %s, %s, \"%s\", \"%s\", \"%s\")" % (session['userID'], DT, sendToID, sendToID, mailTrainUploadDT, headline, content)
    else:
        query = "INSERT INTO mails(SENDERID, DT, RECEIVERID, TRAINID, TRAINDT, HEADLINE, CONTENT) " \
                "VALUES (%s, \"%s\", %s, null, null, \"%s\", \"%s\")" % (session['userID'], DT, sendToID, headline, content)
    res = dbManager.commit(query)
    if res == -1:
        flash('המייל לא נשלח אנא נסה שוב')
        return redirect(request.referrer)
    flash('המייל נשלח בהצלחה!')
    return redirect(request.referrer)
