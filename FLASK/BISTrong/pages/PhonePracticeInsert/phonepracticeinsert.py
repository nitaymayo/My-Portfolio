from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from datetime import datetime

from utilities.db.db_manager import dbManager

# phonepracticeinsert blueprint definition
phonepracticeinsert = Blueprint('phonepracticeinsert', __name__, static_folder='static', static_url_path='/phonepracticeinsert', template_folder='templates')


# Routes
@phonepracticeinsert.route('/InsertPractice', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    platform = request.user_agent.platform
    if platform in ('iphone', 'android', 'blackberry'):
        query = "SELECT * FROM muscle_group_lookup"
        muscles = dbManager.fetch(query)

        return render_template('phonepracticeinsert.html', muscleGroup=muscles)
    else:
        flash('לא ניתן לגשת לעמוד אליו ניסית לגשת')
        return redirect('/homepage')




@phonepracticeinsert.route('/createPractice', methods=['GET', 'POST'])
def createNewPractice():
    type = request.form.get('Type')
    length = request.form.get('Length')
    date = request.form.get('trainDate')
    description = request.form.get('freeWrite')
    UploadDT = datetime.now()
    if type == 'ריצה':
        distance = request.form.get('distance')
        query = "INSERT INTO train(user_id, UploadDT, trainingDate, description, length, distance, type) " \
                "VALUES (%s, \"%s\", \"%s\", \"%s\", %s, %s, \"%s\")" % (
                session['userID'], UploadDT, date, description, length, distance, type)
    else:
        location = request.form.get('place')
        query = "INSERT INTO train(user_id, UploadDT, trainingDate, description, length, location, type) " \
                "VALUES (%s, \"%s\", \"%s\", \"%s\", %s, \"%s\", \"%s\")" % (
                session['userID'], UploadDT, date, description, length, location, type)
    res = dbManager.commit(query)

    if res == -1:
        flash('ישנה בעיה בנתוני האימון, העלת האימון נכשלה')
        return redirect('/InsertPractice')
    else:
        query = "SELECT * FROM muscle_group_lookup"
        muscles = dbManager.fetch(query)
        for muscle in muscles:
            inTrain = request.form.get("%s" % (muscle.muscle_group,))
            if inTrain:
                query = "INSERT INTO muscle_group_in_train(user_id, DT, muscle_group) VALUES " \
                        "(%s, \"%s\", \"%s\")" % (session['userID'], UploadDT, muscle.description)
                res = dbManager.commit(query)

        flash('האימון הועלה בהצלחה, כל הכבוד!')
    return redirect('/InsertPractice')