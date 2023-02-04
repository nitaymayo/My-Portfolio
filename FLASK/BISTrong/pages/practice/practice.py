
from flask import Blueprint, render_template, redirect, url_for, request, session, flash, Flask
from utilities.db.db_manager import dbManager
from flask_mail import Mail, Message
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# practice blueprint definition


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nitaymayo@gmail.com'
app.config['MAIL_PASSWORD'] = 'nitay135'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


practice = Blueprint('practice', __name__, static_folder='static', static_url_path='/practice', template_folder='templates')


# Routes
@practice.route('/categories/<workout>', methods=['GET', 'POST'])
def index(workout):
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')

    workout = workout
    workouDet = dbManager.fetch("SELECT * FROM workout WHERE name = \"%s\"" % (workout,))
    query = "SELECT D.name, D.equipment, DIW.sets, DIW.reps, DIW.rest FROM drill_in_workout AS DIW JOIN drill AS D on D.name = DIW.drill WHERE DIW.workout = \"%s\"" % (workout,)
    drills = dbManager.fetch(query)

    drillString = workouDet[0].name
    drillString = drillString + ": %0a"

    counter = 1
    for drill in drills:
        drillString = str(drillString) + ("%s. %s %s סטים/דקות, %s חזרות, %s מנוחה" % (counter, drill.name, drill.sets, drill.reps, drill.rest)) + "%0a"
        counter = counter + 1

    drillStringWhatsapp = drillString
    drillStringMail = drillString.replace("%0a", "<br>")


    query = "SELECT * FROM saved_workouts WHERE workout = \"%s\" AND user_id = %s" % (workout, session['userID'])
    res = dbManager.fetch(query)
    if res:
        isFavorite = True
    else:
        isFavorite = False

    query = "SELECT muscle_group FROM muscle_group_in_workout WHERE workout = \"%s\"" % (workout,)
    muscleGroups = dbManager.fetch(query)
    return render_template('practice.html', muscleGroups=muscleGroups, workout=workouDet[0], drillStringWhatsapp=drillStringWhatsapp, drillStringMail=drillStringMail, drills=drills, isFavorite=isFavorite)

@practice.route('/deleteWorkout', methods=['GET', 'POST'])
def deleteWorkout():
    if not session['manager']:
        return redirect('/practice')
    workout = request.args.get('workout')
    query = "SELECT category FROM workout WHERE name = \"%s\"" % (workout,)
    category = dbManager.fetch(query)
    query = "DELETE FROM drill_in_workout WHERE workout = \"%s\"" % (workout,)
    drillsRes = dbManager.commit(query)
    query = "DELETE FROM muscle_group_in_workout WHERE workout = \"%s\"" % (workout,)
    muscleres = dbManager.commit(query)
    query = "DELETE FROM saved_workouts WHERE workout = \"%s\"" % (workout,)
    res = dbManager.commit(query)
    query = "DELETE FROM workout WHERE name = \"%s\"" % (workout,)
    workoutRes = dbManager.commit(query)
    if (drillsRes == (-1)) or (workoutRes == (-1)):
        flash('מחיקת האימון נכשלה')
        return redirect(url_for('practice.index', workout=workout, category=category[0].category))
    else:
        flash('אימון נמחק בהצלחה')
        return redirect(url_for('categorypage.index', category=category[0].category))

@practice.route('/saveFavorite', methods=['GET', 'POST'])
def save_unsave_favorite():
    favorite = request.args.get('favorite')
    workout = request.args.get('workout')

    if favorite == 'True':
        query = "DELETE FROM saved_workouts WHERE user_id = %s AND workout = \"%s\"" % (session['userID'], workout)
    else:
        query = "INSERT INTO saved_workouts(user_id, workout) VALUES (%s, \"%s\")" % (session['userID'], workout)
    res = dbManager.commit(query)
    if res == 1:
        if favorite == 'True':
            flash('אימון נמחק בהצלחה מהמועדפים')
        else:
            flash('אימון נוסף בהצלחה למועדפים!')
    else:
        flash('משהו השתבש, בבקשה נסה שנית')
    return redirect(request.referrer)


@practice.route('/sendPracticeMail', methods=['GET', 'POST'])
def sendPracticeMail():
    if request.args.__contains__('email'):
        query = "UPDATE user SET email = \"%s\" WHERE user_id = %s" % (request.args.get('email'), session['userID'])
        res = dbManager.commit(query)
        if res == 1:
            session['userEmail'] = request.args.get('email')
        toMail = request.args.get('email')
    else:
        toMail = session['userEmail']

    content = request.args.get('content')

    msg = MIMEMultipart('alternative')
    content = "תודה שהשתמשת בBISTrong!" + " <br> " + content
    msg["Subject"] = "האימון שלך"
    msg["From"] = "BISTrongAssistant@gmail.com"
    msg["To"] = toMail
    html = "<div style='direction:rtl'>" + content + "</div>"
    part1 = MIMEText(content, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg["From"], "n9dvbDfu")

            smtp.send_message(msg)
            flash('מייל נשלח בהצלחה!')
    except:
        flash('ישנה שגיאה, המייל לא נשלח')

    return redirect(request.referrer)
