from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db.userDataPuller import userDataPuller

# login blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    user = userDataPuller.checkUsernameNPassword(username, password)
    if user and len(user):
        session['logged_in'] = True
        session['first_name'] = user[0].First_Name
        session['user_id'] = user[0].Customer_ID
        session['user'] = {
            'username': user[0].username,
            'last_name': user[0].Last_Name,
            'user_ID': user[0].Customer_ID,
            'email': user[0].Email,
        }
        return redirect(url_for('homepage.index'))
    return render_template('page_not_found.html', errmsg='login failed')
