from flask import Blueprint, render_template, session

# logout blueprint definition
logout = Blueprint('logout', __name__, static_folder='static', static_url_path='/logout', template_folder='templates')


@logout.route('/logout')
def index():
    session.clear()
    return  render_template('logout.html')
