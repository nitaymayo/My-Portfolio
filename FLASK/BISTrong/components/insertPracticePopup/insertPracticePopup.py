from flask import Blueprint, render_template

# insertPracticePopup blueprint definition
insertPracticePopup = Blueprint('insertPracticePopup', __name__, static_folder='static', static_url_path='/insertPracticePopup', template_folder='templates')


