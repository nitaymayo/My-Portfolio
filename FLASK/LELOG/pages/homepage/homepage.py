from flask import Blueprint, render_template, redirect, url_for, request, session
from utilities.db.itemsManager import itemsManager

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    query_prod = itemsManager.getTable('products')
    query_rec = itemsManager.getTable('recipes')
    query_art = itemsManager.getTable('articles')

    prod = [query_prod[0], query_prod[1], query_prod[2]]
    rec = [query_rec[0], query_rec[1], query_rec[2]]
    art = [query_art[0], query_art[2]]

    return render_template('homepage.html', products=prod, recipes=rec, articles=art)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))


