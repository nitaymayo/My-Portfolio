from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from utilities.db.db_manager import dbManager
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath

# drillspage blueprint definition
drillspage = Blueprint('drillspage', __name__, static_folder='static', static_url_path='/drillspage',
                       template_folder='templates')
app = Flask(__name__)


# Routes
@drillspage.route('/drillspage', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    categories = dbManager.fetch('SELECT DISTINCT muscle_group FROM muscle_group_lookup')
    catName = {}
    drills = {}
    for group in categories:
        drills[group.muscle_group] = dbManager.fetch(f"SELECT * FROM drill WHERE muscle_group = '{group[0]}'")
        query = f"SELECT description FROM muscle_group_lookup WHERE muscle_group = '{group[0]}'"
        catName[group.muscle_group] = dbManager.fetch(query)
    return render_template('drillspage.html', drillsByCat=drills, catName=catName)



UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/media/drillVideos')
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

@drillspage.route('/createNewDrill', methods=['GET', 'POST'])
def createDrill():
    name = request.form['drillNameInput']
    muscleDesc = request.form['muscleGroupInput']
    muscle = dbManager.fetch('SELECT muscle_group FROM muscle_group_lookup where description = \"%s\"' % (muscleDesc,))
    if muscle:
        muscle = muscle[0].muscle_group
    equip = request.form['equipmentInput']
    description = request.form['descriptionInput']
    video = request.files['videoInsertInput']
    videoName = secure_filename(video.filename)
    if videoName:
        video.save(os.path.join(app.config['UPLOAD_FOLDER'], videoName))
    query = "INSERT INTO drill VALUES (\"%s\" , \"%s\" , \"%s\" , \"%s\" , \"%s\" )" % (
    name, muscle, equip, description, videoName)
    res = dbManager.commit(query)
    if res == '-1':
        flash("משהו השתבש, הוספת התרגיל נכשלה")
    else:
        flash("תרגיל נוסף בהצלחה!")
    return redirect(url_for('drillspage.index'))


@drillspage.route('/deleteDrill')
def deleteDrill():
    drill = request.args['drill']
    query = "SELECT video FROM drill WHERE name=\"%s\"" % (drill,)
    videoName = dbManager.fetch(query)[0].video
    if videoName:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], videoName))
    query = "DELETE FROM drill WHERE name = \"%s\"" % (drill,)
    res = dbManager.commit(query)
    if res == -1:
        flash('לא ניתן למחוק את התרגיל מכיוון שהוא חלק מאימון.')
    else:
        flash('תרגיל נמחק בהצלחה')
    return redirect(url_for('drillspage.index'))
