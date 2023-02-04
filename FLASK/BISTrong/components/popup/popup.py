from flask import Blueprint, render_template

# popup blueprint definition
popup = Blueprint('popup', __name__, static_folder='static', static_url_path='/popup', template_folder='templates')
