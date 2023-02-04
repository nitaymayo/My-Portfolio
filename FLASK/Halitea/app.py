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

## shop
from pages.shop.shop import shop
app.register_blueprint(shop)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## header
from components.header.header import header
app.register_blueprint(header)

## footer
from components.footer.footer import footer
app.register_blueprint(footer)