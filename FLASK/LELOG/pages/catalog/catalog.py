from flask import Blueprint, render_template, request
from utilities.db.itemsManager import itemsManager

# catalog blueprint definition
catalog = Blueprint('catalog',
                    __name__,
                    static_folder='static',
                    static_url_path='/catalog',
                    template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    if 'cat_id' in request.args:
        cat_id = request.args['cat_id']
        query_res = ''
        if cat_id == '1':
            query_res = itemsManager.getTable("Products")
        if cat_id == '2':
            query_res = itemsManager.getTable("Recipes")
        if cat_id == '3':
            query_res = itemsManager.getTable("Articles")
        return render_template('catalog.html', cat_id=cat_id, items=query_res)
    return render_template('catalog.html')
