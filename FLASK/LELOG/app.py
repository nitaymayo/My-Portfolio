from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Recipe
from pages.recipe.recipe import recipe
app.register_blueprint(recipe)

## Article
from pages.article.article import article
app.register_blueprint(article)

## product
from pages.product.product import product
app.register_blueprint(product)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)


###### Components

## header
from components.header.header import header
app.register_blueprint(header)

## footer
from components.footer.footer import footer
app.register_blueprint(footer)

## login
from components.login.login import login
app.register_blueprint(login)

## alreadyloggedmsg
from components.alreadyloggedmsg.alreadyloggedmsg import alreadyloggedmsg
app.register_blueprint(alreadyloggedmsg)

## logout
from components.logout.logout import logout
app.register_blueprint(logout)

## signin
from components.signin.signin import signin
app.register_blueprint(signin)

