from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from datetime import datetime
from utilities.db.db_manager import dbManager

# header blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')

@header.route('/newTrain', methods=['GET', 'POST'])
def insertTrain():
    type = request.form.get('Type')
    length = request.form.get('Time')
    date = request.form.get('Date')
    description = request.form.get('freeWrite')
    UploadDT = datetime.now()
    if type == 'ריצה':
        distance = request.form.get('Distance')
        query = "INSERT INTO train(USER_ID, UPLOADDT, TRAININGDATE, DESCRIPTION, LENGTH, DISTANCE, TYPE) " \
                "VALUES (%s, \"%s\", \"%s\", \"%s\", %s, %s, \"%s\")" % (session['userID'], UploadDT, date, description, length, distance, type)
    else:
        location = request.form.get('place')
        query = "INSERT INTO train(USER_ID, UPLOADDT, TRAININGDATE, DESCRIPTION, LENGTH, LOCATION, TYPE) " \
                "VALUES (%s, \"%s\", \"%s\", \"%s\", %s, \"%s\", \"%s\")" % (session['userID'], UploadDT, date, description, length, location, type)
    res = dbManager.commit(query)

    if res == -1:
        flash('ישנה בעיה בנתוני האימון, העלת האימון נכשלה')
        return redirect('/homepage')
    else:
        counter = 0
        while request.form.__contains__('nameMuscleGroup%s' % (counter,)):
            muscleName = request.form.get('nameMuscleGroup%s' % (counter,))
            query = "INSERT INTO muscle_group_in_train(USER_ID, DT, MUSCLE_GROUP) VALUES " \
                    "(%s, \"%s\", \"%s\")" % (session['userID'], UploadDT, muscleName)
            res = dbManager.commit(query)
            counter = counter+1
            if res == -1:
                flash('בעיה בהכנסת האימון, בדוק האם קבוצות השריר הוכנסו נכון')
                query = "DELETE FROM muscle_group_in_train " \
                        "WHERE user_id = %s AND DT = \"%s\"" % (session['userID'], UploadDT)
                dbManager.commit(query)
                query = "DELETE FROM train " \
                        "WHERE user_id = %s AND UploadDT = \"%s\"" % (session['userID'], UploadDT)
                dbManager.commit(query)
                return redirect('/homepage')
        flash('האימון הועלה בהצלחה, כל הכבוד!')
    return redirect('/homepage')
