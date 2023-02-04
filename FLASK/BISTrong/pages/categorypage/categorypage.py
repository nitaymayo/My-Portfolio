from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from utilities.db.db_manager import dbManager

# categorypage blueprint definition
categorypage = Blueprint('categorypage', __name__, static_folder='static', static_url_path='/categorypage', template_folder='templates')


# Routes
@categorypage.route('/categorypage', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    category = request.args['category']
    workouts_to_show = dbManager.fetch("SELECT W.name, W.description, W.length FROM workout as W WHERE"
                                       " W.category=\"%s\"" % (category,))
    if not workouts_to_show:
        flash('אין תרגילים בקטגוריה זו')
        return redirect(url_for('categories.index'))

    query = "SELECT * FROM saved_categories WHERE user_id = %s AND category = \"%s\"" % (session['userID'], category)
    res = dbManager.fetch(query)
    isFavorite = False
    if res:
        isFavorite = True
    else:
        isFavorite = False

    categoryDet = dbManager.fetch("SELECT * FROM workout_category_lookup WHERE category='%s'" % (category,))
    return render_template('categorypage.html', workouts=workouts_to_show, isFavorite=isFavorite, category=categoryDet)


@categorypage.route('/saveCategory', methods=['GET', 'POST'])
def save_unsave_category():
    category = request.args.get('category')
    query = "SELECT * FROM saved_categories WHERE category = \"%s\"" % (category,)
    res = dbManager.fetch(query)
    if res:
        query = "DELETE FROM saved_categories WHERE category = \"%s\" AND user_id = \"%s\"" % (category, session['userID'])
        res = dbManager.commit(query)
        if res == 1:
            flash('הקטגוריה יצאה בהצלחה מרשימת המועדפים')
        else:
            flash('משהו השתבש, נסה שנית')
    else:
        query = "INSERT INTO saved_categories(user_id, category) VALUES (%s, \"%s\")" % (session['userID'], category)
        res = dbManager.commit(query)
        if res == 1:
            flash('הקטגוריה נוספה למועדפים בהצלחה')
        else:
            flash('משהו השתבש, נסה שנית')

    return redirect(request.referrer)

