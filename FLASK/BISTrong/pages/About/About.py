from flask import Blueprint, render_template, redirect, url_for, session, flash

# about blueprint definition
about = Blueprint('about', __name__, static_folder='static', static_url_path='/about', template_folder='templates')


# Routes
@about.route('/about', methods=['GET', 'POST'])
def index():
    if not session:
        flash("יש להתחבר לפני שימוש באתר")
        return redirect('/')
    return render_template('about.html')

