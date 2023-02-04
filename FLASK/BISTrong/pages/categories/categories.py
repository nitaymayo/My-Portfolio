from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.db.db_manager import dbManager

# categories blueprint definition
categories = Blueprint('categories', __name__, static_folder='static', static_url_path='/categories', template_folder='templates')


# Routes
@categories.route('/categories', methods=['GET', 'POST'])
def index():
    if not session:
        flash('יש להתחבר לפני שימוש באתר')
        return redirect('/')
    categories_to_show = dbManager.fetch("SELECT * FROM workout_category_lookup")
    drills = dbManager.fetch("SELECT * FROM drill")
    query = "SELECT * FROM muscle_group_lookup"
    muscles = dbManager.fetch(query)
    return render_template('categories.html', muscleGroup=muscles, categories=categories_to_show, drills=drills)

@categories.route('/createNewPractice', methods=['GET', 'POST'])
def newPractice():
    name = request.args['practiceNameInput']
    query = "SELECT name FROM workout WHERE name = \"%s\"" % (name,)
    res = dbManager.fetch(query)
    if res:
        flash("כבר קיים אימון עם שם זהה, בבקשה לבחור שם אחר")
        return redirect(url_for('categories.index'))
    length = request.args['practiceLengthInput']
    category = request.args['practiceCategoryInput']
    intensitiy = request.args['practiceIntensityInput']
    type = request.args['practiceType']
    descreption = request.args['newPracticeDescriptionInput']
    note = request.args['newPracticeNoteInput']
    query = "INSERT INTO workout(name, length, category, type, description, intensity, note) VALUES"\
            " (\"%s\", %s, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\" )" % (name, length, category, type, descreption, intensitiy, note)
    res = dbManager.commit(query)
    if res == -1:
        flash('בעיה בנתוני האימון, אימון לא נכנס אנא הכנס שוב')
        return redirect(url_for('categories.index'))
    counter = 0
    has_more_drills = True
    while has_more_drills:
        query = "INSERT INTO drill_in_workout(workout, drill, sets, reps,  rest) VALUES"\
                " (\"%s\", \"%s\", %s, %s, %s)" % (name, request.args['nameDrill%s' % counter], request.args['setsDrill%s' % counter], request.args['repsDrill%s' % counter], request.args['restDrill%s' % counter])
        drillres = dbManager.commit(query)
        if drillres == -1:
            flash('בעיה בהכנסת תרגילי האימון, האימון נמחק בבקשה הכנס שוב')
            query = "DELETE FROM drill_in_workout WHERE workout = \"%s\"" % (name,)
            dbManager.commit(query)
            query = "DELETE FROM workout WHERE name = \"%s\"" % (name,)
            dbManager.commit(query)
            return redirect(url_for('categories.index'))
        if not request.args.__contains__('nameDrill%s' % (counter+1)):
            has_more_drills = False
        else:
            counter = counter + 1

    query = "SELECT * FROM muscle_group_lookup"
    muscles = dbManager.fetch(query)
    for muscle in muscles:
        inTrain = request.args.get("%s" % (muscle.muscle_group,))
        if inTrain:
            query = "INSERT INTO muscle_group_in_workout(workout, muscle_group) VALUES " \
                    "(\"%s\", \"%s\")" % (name, muscle.description)
            res = dbManager.commit(query)

    flash("אימון נוסף בהצלחה!")
    return redirect(url_for('categories.index'))


@categories.route('/createNewCategory', methods=['GET', 'POST'])
def newCategory():
    name = request.args['CategoryNameInput']
    intensity = request.args['CategoryLevelInput']
    goal = request.args['CategoryGoalInput']
    description = request.args['newCategoryDescriptionInput']
    query = "INSERT INTO workout_category_lookup(category, description, intensity, goal) VALUES"\
            " (\"%s\", \"%s\", \"%s\", \"%s\")" % (name, description, intensity, goal)
    res = dbManager.commit(query)
    msg = False
    if res == -1:
        flash("יצירת הקטגוריה נכשלה, אנא נסה שנית")
    else:
        flash("קטגוריה נוצרה בהצלחה!")
    return redirect(url_for("categories.index"))


@categories.route('/deleteCategory', methods=['GET', 'POST'])
def deleteCategory():
    category = request.args['category']
    query = "DELETE FROM drill_in_workout WHERE workout IN (SELECT W.name FROM workout AS W WHERE category = \"%s\")" % (category,)
    res = dbManager.commit(query)
    query = "DELETE FROM muscle_group_in_workout WHERE workout IN (SELECT W.name FROM workout AS W WHERE category = \"%s\")" % (
    category,)
    res = dbManager.commit(query)
    query = "DELETE FROM workout WHERE category = \"%s\"" % (category,)
    res = dbManager.commit(query)
    query = "DELETE FROM saved_categories WHERE category = \"%s\"" % (category,)
    res = dbManager.commit(query)
    query = "DELETE FROM workout_category_lookup WHERE category = \"%s\"" % (category,)
    res = dbManager.commit(query)
    msg = False
    if res == -1:
        flash("בעיה במחיקת הקטגוריה, נסה שנית")
    else:
        flash("קטגורית %s נמחקה בהצלחה!" % (category,))
    return redirect(url_for("categories.index"))
