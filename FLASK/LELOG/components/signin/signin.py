from flask import Blueprint, render_template, request, session
from utilities.db.userDataPuller import userDataPuller

# signin blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


@signin.route('/signin', methods=['GET', 'POST'])
def index():
    count_user = userDataPuller.userscount()
    insert = userDataPuller.insert(request.form['email'], request.form['password'], request.form['first_name'], request.form['last_name'], request.form['phone_number'], request.form['username'])
    if insert > 0:
        session['logged_in'] = True
        session['first_name'] = request.form['first_name']
        session['user_id'] = count_user+1
        session['user'] = {
            'username': request.form['username'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
        return render_template('sucssessignin.html')
    return render_template('page_not_found.html', errmsg='Sign up failed')

