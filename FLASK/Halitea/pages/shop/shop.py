from flask import Blueprint, render_template, request, jsonify
from utilities.db.db_manager import dbManager
import urllib3

# shop blueprint definition
shop = Blueprint('shop', __name__, static_folder='static', static_url_path='/shop', template_folder='templates')


# Routes
@shop.route('/shop')
def index():
    return render_template('shop.html')


@shop.route('/order', methods=['POST'])
def order():
    response = request.get_json()
    size = response['size']

    ingredients = tuple(response['items'])



    query = "SELECT SUM(%s_price) AS TOTAL " \
            "FROM ingredient AS I " \
            "WHERE I.name IN %s" % (size, ingredients)
    totalprice = dbManager.fetch(query)[0].TOTAL

    return {'1': '2'}, 200

# @shop.route('/getcities', methods=['POST'])
# def getcities():
#     url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=bf185c7f-1a4e-4662-88c5-fa118a244bda&city_name:אודים'
#     fileobj =  (url)
#     fileobj.read()
#     return