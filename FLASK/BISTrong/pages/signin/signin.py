from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.db.db_manager import dbManager

# signin blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')
signinMOBILE = Blueprint('signinMOBILE', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


# Routes
@signin.route('/', methods=['GET', 'POST'])
def index():
    platform = request.user_agent.platform
    if platform in ('iphone', 'android', 'blackberry'):
        return render_template('signinMOBILE.html')
    else:
        return render_template('signin.html')


@signin.route('/signin', methods=['GET', 'POST'])
def signinfunc():
    uname = request.form['username']
    password = request.form['password']
    ans = dbManager.fetch(f"SELECT * FROM user WHERE user_id='{uname}' AND password='{password}'")
    sucsess = False
    if ans:
        session['userID'] = uname
        if ans[0].admin == 1:
            session['manager'] = True
        else:
            session['manager'] = False

        session['userCourse'] = ans[0].course
        session['userEmail'] = ans[0].email
        sucsess = True

    if sucsess:
        platform = request.user_agent.platform
        if platform in ('iphone', 'android', 'blackberry'):
            return redirect(url_for('phonepracticeinsert.index'))
        else:
            return redirect('/homepage')
    else:
        flash('הנתונים שהוזנו שגויים')
        return redirect(url_for('signin.index'))

@signin.route('/logout', methods=['GET', 'POST'])
def logoutfunc():
    session.clear()
    return redirect('/')
