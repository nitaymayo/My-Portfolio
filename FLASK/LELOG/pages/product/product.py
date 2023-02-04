from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db.itemsManager import productHandler
from utilities.db.wishListManager import wishListManager

# product blueprint definition
product = Blueprint('product',
                    __name__,
                    static_folder='static',
                    static_url_path='/product',
                    template_folder='templates')


# Routes
@product.route('/product')
def index():
        if 'prod_id' in request.args:
            prod_id = request.args['prod_id']
            query_res = productHandler.pullProduct(prod_id)[0]
            inwish = False
            if len(session) > 0:
                if wishListManager.exist(session['user_id'], prod_id):
                    inwish = True
            if query_res:
                return render_template('product.html', product=query_res, inwish=inwish)
        return render_template('product.html')


@product.route('/product/wishlist')
def addtowish():
    user_id = session['user_id']
    prod_id = request.args['prod_id']

    if wishListManager.exist(user_id, prod_id):
        query_sucsses = wishListManager.delete(user_id, prod_id)
    else:
        query_sucsses = wishListManager.insert(user_id, prod_id)
    return redirect('/product?prod_id=%s' % (request.args['prod_id']))



