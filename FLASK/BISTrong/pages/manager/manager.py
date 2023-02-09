from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from utilities.db.db_manager import dbManager

# manager blueprint definition
manager = Blueprint('manager', __name__, static_folder='static', static_url_path='/manager', template_folder='templates')


# Routes
@manager.route('/manager', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    course = False
    megama = False
    trainees = False
    query2 = False
    traineeVars = {}
    dateString = ""
    dateVars = {}
    selectQuery = "SELECT T.trainingDate, T.length, T.description, T.location, T.type, T.distance, U.name, U.profile_picture, U.user_id, T.UploadDT FROM train AS T JOIN user AS U on U.user_id = T.user_id  "
    if request.args.__contains__('fromDate'):
        fromDate = request.args.get('fromDate')
        toDate = request.args.get('toDate')
        dateVars['from'] = fromDate
        dateVars['to'] = toDate
        dateString = "AND T.trainingDate BETWEEN \"%s\" AND \"%s\"" % (fromDate, toDate)



    if request.args.__contains__('course'):
        course = request.args.get('course')
        if request.args.__contains__('megama'):
            megama = request.args.get('megama')
            query2 = "SELECT user_id, name FROM user WHERE course = \"%s\" AND megama = \"%s\"" % (course, megama)
            if request.args.__contains__('trainee'):
                user = request.args.get('trainee')
                whereQuery = "WHERE U.course = \"%s\" AND U.megama = \"%s\" AND T.user_id = %s %s ORDER BY " \
                                "T.trainingDate DESC" % (course, megama, user, dateString)
                traineeNameQuery = 'SELECT name, user_id FROM user WHERE user_id = %s' % (user,)
                res = dbManager.fetch(traineeNameQuery)
                traineeVars['name'] = res[0].name
                traineeVars['id'] = res[0].user_id
            else:
                whereQuery = "WHERE U.course = \"%s\" AND U.megama = \"%s\" %s" \
                        "ORDER BY T.trainingDate DESC" % (course, megama, dateString)
        else:
            whereQuery =  "WHERE U.course = \"%s\" %s " \
                "ORDER BY T.trainingDate DESC" % (course, dateString)
    else:
        whereQuery = "WHERE U.course IS NOT NULL %s" \
                "ORDER BY T.trainingDate DESC" % (dateString,)
    res = dbManager.fetch(selectQuery + whereQuery)
    if query2:
        trainees = dbManager.fetch(query2)
    trainDays = {}
    day = ""
    if res:
        for train in res:
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

    muscleGroup = {}
    if res:
        for train in res:
            query = "SELECT muscle_group FROM muscle_group_in_train WHERE user_id = %s AND DT = \"%s\"" % (train.user_id, train.UploadDT)
            muscleGroup[train] = dbManager.fetch(query)

    return render_template('manager.html', trains=res, dateVars=dateVars, course=course, trainees=trainees, megama=megama, traineeVars=traineeVars, muscleGroup=muscleGroup, trainDays=trainDays)


@manager.route('/addUsers', methods=['GET', 'POST'])
def addUsers():
    counter = 0
    assigned = 0
    while request.form.__contains__('userID%s' % (counter,)):
        ID = request.form.get('userID%s' % (counter,))
        admin = request.form.get('isAdmin%s' % (counter,))
        if not admin:
            admin = False
        query = "INSERT INTO user(user_id, password, admin) VALUES " \
                "(%s, \"%s\", %s)" % (ID, ID, admin)
        res = dbManager.commit(query)
        counter = counter + 1
        if res == -1:
            flash('בעיה ביצירת משתמש עבור תז: ' + ID)
        else:
            assigned = assigned + 1
    flash('תהליך ההרשמה הסתיים, %s משתמשים חדשים נוספו' % (assigned,))

    return redirect('/manager')
