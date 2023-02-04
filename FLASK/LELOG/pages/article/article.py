from flask import Blueprint, render_template, request
from utilities.db.itemsManager import articleHandler

# article blueprint definition
article = Blueprint('article',
                    __name__,
                    static_folder='static',
                    static_url_path='/article',
                    template_folder='templates')


# Routes
@article.route('/article')
def index():
    if 'article_id' in request.args:
        art_id = request.args['article_id']
        query_res = articleHandler.pullArticle(art_id)
        return render_template('article.html', article=query_res[0])
    return render_template('article.html')
