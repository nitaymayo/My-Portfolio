from flask import Blueprint, render_template, session, request, redirect
from utilities.db.userDataPuller import userDataPuller
from utilities.db.wishListManager import wishListManager
from utilities.db.itemsManager import itemsManager

# profile page blueprint definition
profile = Blueprint('profile',
                    __name__,
                    static_folder='static',
                    static_url_path='/profile',
                    template_folder='templates')


# Routes
@profile.route('/profile')
def index():
    user = userDataPuller.pulldata(session['user_id'])
    wish_list = wishListManager.getFavorites(session['user_id'])
    products = itemsManager.getTableByLimit('products', 0, 3)
    recipes = itemsManager.getTableByLimit('recipes', 0, 3)
    summary = userDataPuller.Summary(session['user_id'])
    return render_template('profile.html', user=user, wish_list=wish_list, fav_recipes=recipes, bought_prod=products, summary=summary)

@profile.route('/clearwish')
def clearwish():
    wishListManager.deleteAllFor(session['user_id'])
    return redirect('/profile')


@profile.route('/profile/update', methods=['GET', 'POST'])
def update():
    querysucsses = userDataPuller.update(request.form['email'], request.form['password'], request.form['first_name'], request.form['last_name'], request.form['phone_number'], session['user_id'])
    user = userDataPuller.pulldata(session['user_id'])
    msg = 'something went wrong, data not updated'
    if querysucsses == 1:
        msg = 'data updated sucssesfuly'
    wish_list = wishListManager.getFavorites(session['user_id'])
    prod_arr = itemsManager.getTable('products')
    products = itemsManager.getTableByLimit('products', 0, 3)
    recipes = itemsManager.getTableByLimit('recipes', 0, 3)
    summary = userDataPuller.Summary(session['user_id'])
    return render_template('profile.html', user=user, msg=msg, wish_list=wish_list, fav_recipes=recipes, bought_prod=products, summary=summary)
