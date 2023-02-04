from flask import Blueprint, render_template

# footer blueprint definition
footer = Blueprint('footer', __name__, static_folder='static', static_url_path='/footer', template_folder='templates')
