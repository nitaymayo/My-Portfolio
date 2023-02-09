from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.db.db_manager import dbManager

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/homepage', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    if session['manager']:
        query = "SELECT U.profile_picture, U.name, T.trainingDate, T.description, T.distance, T.length, T.type, T.location " \
                "FROM train AS T JOIN user AS U on U.user_id = T.user_id " \
                "ORDER BY T.trainingDate DESC"
    else:
        query = "SELECT U.profile_picture, U.name, T.trainingDate, T.description, T.distance, T.length, T.type, T.location " \
                "FROM train AS T JOIN user AS U on U.user_id = T.user_id WHERE U.course = \"%s\"" \
                "ORDER BY T.trainingDate DESC" % (session['userCourse'],)
    All_Posts = dbManager.fetch(query)
    trainDays = {}
    day = ""
    for train in All_Posts:
        trainDay = train.trainingDate.weekday()
        if trainDay == 0:
            day = 'שני'
        elif trainDay == 1:
            day = 'שלישי'
        elif trainDay == 2:
            day = 'רביעי'
        elif trainDay == 3:
            day = 'חמישי'
        elif trainDay == 4:
            day = 'שישי'
        elif trainDay == 5:
            day = 'שבת'
        elif trainDay == 6:
            day = 'ראשון'
        trainDays[train] = day
    total_trainees = dbManager.fetch('SELECT count(*) as num FROM user;')
    total_hours = dbManager.fetch('SELECT CAST(SUM(length)/60 AS DECIMAL(10,2)) as num FROM train')
    total_KM = dbManager.fetch('SELECT SUM(distance) as num FROM train')
    query = "SELECT COUNT(*) as num FROM mails WHERE isNew = true AND receiverID = " + session['userID']
    session['newMails'] = dbManager.fetch(query)
    if session['newMails']:
        session['newMails'] = session['newMails'][0].num
    else:
        session['newMails'] = 0

    query = "SELECT description as name FROM muscle_group_lookup"
    muscleGroupsName = dbManager.fetch(query)

    query = "SELECT * FROM user WHERE user_id = " + session['userID']
    detPopup = {}
    user = dbManager.fetch(query)
    if user[0].name == None:
        detPopup = user[0]


    return render_template('homepage.html', posts=All_Posts, user=detPopup, muscleGroupsName=muscleGroupsName, trainDays=trainDays, total_trainers=total_trainees[0].num, total_hours=total_hours[0].num, total_KM=total_KM[0].num)

