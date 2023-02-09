from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from utilities.db.db_manager import dbManager
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
from django.core.serializers.json import DjangoJSONEncoder
import json
from datetime import datetime


# personal blueprint definition
personal = Blueprint('personal', __name__, static_folder='static', static_url_path='/personal', template_folder='templates')


# Routes
@personal.route('/personal', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    query = "SELECT * FROM user WHERE user_id = " + session['userID']
    user = dbManager.fetch(query)

    allVars = {
        'totalRun': 0,
        'totalDist': 0,
        'totalRunLength': 0,
        'avgPace': 0,
        'totalPower': 0,
        'preferredPlace': 0,
        'totalPowerLength': 0,
        'preferredMuscle': 0
    }

    favoritePlace = {}

    query = "SELECT T.*, DL.day_name FROM train as T join date_lookup AS DL on DL.date = T.trainingDate WHERE user_id = " + session['userID']
    trains = dbManager.fetch(query)
    if trains:
        for tr in trains:
            if tr.type == 'ריצה':
                allVars['totalRun'] = allVars['totalRun'] + 1
                allVars['totalDist'] = allVars['totalDist'] + tr.distance
                allVars['totalRunLength'] = allVars['totalRunLength'] + tr.length
            else:
                allVars['totalPower'] = allVars['totalPower'] + 1
                allVars['totalPowerLength'] = allVars['totalPowerLength'] + tr.length
                if favoritePlace.__contains__(tr.location):
                    favoritePlace[tr.location] = favoritePlace[tr.location] + 1
                else:
                    favoritePlace[tr.location] = 1
        if favoritePlace:
            allVars['preferredPlace'] = max(favoritePlace, key=favoritePlace.get)
        else:
            allVars['preferredPlace'] = "ללא"

        query = "SELECT muscle_group, COUNT(*) AS NUM " \
                "FROM train as T " \
                "join muscle_group_in_train AS MG on T.user_id = MG.user_id and T.UploadDT = MG.DT " \
                "WHERE T.user_id = %s " \
                "GROUP BY muscle_group " \
                "ORDER BY 2 DESC " \
                "LIMIT 1" % (session['userID'])
        res = dbManager.fetch(query)
        if res:
            allVars['preferredMuscle'] = res[0].muscle_group
        else:
            allVars['preferredMuscle'] = 'ללא'


        allVars['AVG'] = round((allVars['totalRunLength'] + allVars['totalPowerLength']) / (allVars['totalRun'] + allVars['totalPower']),2)
        if allVars['totalDist']:
            allVars['avgPace'] = round(allVars['totalRunLength']/allVars['totalDist'], 2)

    #אימונים מועדפים
    query = "SELECT W.category, W.name, W.length " \
            "FROM workout AS W " \
            "JOIN saved_workouts as SW on W.name = SW.workout " \
            "WHERE SW.user_id = %s" % (session['userID'],)
    allVars['favoriteWorkouts'] = dbManager.fetch(query)

    # קטגוריות מועדפים
    query = "SELECT W.category, W.goal, W.intensity " \
            "FROM workout_category_lookup AS W " \
            "JOIN saved_categories AS SC on W.category = SC.category " \
            "WHERE SC.user_id = %s" % (session['userID'],)
    allVars['favoriteCategories'] = dbManager.fetch(query)

    query = "SELECT DL.period " \
            "FROM date_lookup as DL " \
            "WHERE date = \"%s\"" % (datetime.today().strftime('%Y-%m-%d'),)
    currentPeriod = dbManager.fetch(query)[0].period

    query = "SELECT DL.week, count(*) AS NUM " \
            "FROM train as T " \
            "join date_lookup AS DL on DL.date = T.trainingDate " \
            "WHERE user_id = %s AND " \
            "DL.period = \"%s\" " \
            "GROUP BY DL.week " \
            "ORDER BY 1 desc " % (session['userID'], currentPeriod)
    weeklyTraining = dbManager.fetch(query)
    temp = {}
    for i in range(1,27):
        temp[i] = 0

    for i in weeklyTraining:
        temp[i.week] = i.NUM

    allVars['maxTrain'] = max(temp.values())

    temp = json.dumps(temp, cls=DjangoJSONEncoder)

    return render_template('personal.html', user=user[0], weeklyTraining=temp, trains=trains, allVars=allVars)

app = Flask(__name__)

UPLOADS_PATH = join(dirname(realpath(__file__)), '../../static/media/img/profileImg')
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

@personal.route('/personal/UpdateData', methods=['GET', 'POST'])
def UpdateData():
    name = request.form.get('name').strip()
    course = request.form.get('course')
    email = request.form.get('email').strip()
    password = request.form.get('password').strip()
    megama = request.form.get('megama').strip()
    weight = request.form.get('weight')

    profilePicture = request.files.get('profilePicture')




    profileQuery = ""

    if profilePicture:
        query = "SELECT profile_picture FROM user WHERE user_id = " + session['userID']
        currentImg = dbManager.fetch(query)
        if currentImg[0].profile_picture:
            currentImg = currentImg[0].profile_picture
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], currentImg))
            query = "UPDATE user SET profile_picture = Null WHERE user_id = " + session['userID']
            dbManager.commit(query)
        pictureName = secure_filename(profilePicture.filename)
        profileQuery = ", profile_picture = \"%s\"" % (pictureName,)

    session['userEmail'] = email

    query = "UPDATE user " \
            "SET name = \"%s\", " \
                 "course = \"%s\", " \
                 "email = \"%s\", " \
                 "password = \"%s\", " \
                 "megama = \"%s\", " \
                 "weight = %s %s " \
            "WHERE user_id = %s" % (name, course, email, password, megama, weight, profileQuery, session['userID'])
    res = dbManager.commit(query)

    if res == 1 or res == 0:
        if profilePicture:
            if pictureName:
                profilePicture.save(os.path.join(app.config['UPLOAD_FOLDER'], pictureName))
        flash('הנתונים עודכנו בהצלחה')
        session['userCourse'] = course
    else:
        flash('בעיה בעדכון הנתונים, אין עדכון')

    return redirect('/personal')
