from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## SignIn
from pages.signin.signin import signin, signinMOBILE
app.register_blueprint(signin)
app.register_blueprint(signinMOBILE)

## categories
from pages.categories.categories import categories
app.register_blueprint(categories)

## categorypage
from pages.categorypage.categorypage import categorypage
app.register_blueprint(categorypage)

## practice
from pages.practice.practice import practice
app.register_blueprint(practice)

## personal
from pages.personal.personal import personal
app.register_blueprint(personal)

## drillspage
from pages.drillsPage.drillsPage import drillspage
app.register_blueprint(drillspage)

## About
from pages.About.About import about
app.register_blueprint(about)

## mail
from pages.mail.mail import mail
app.register_blueprint(mail)

## manager
from pages.manager.manager import manager
app.register_blueprint(manager)

## phonepracticeinsert
from pages.PhonePracticeInsert.phonepracticeinsert import phonepracticeinsert
app.register_blueprint(phonepracticeinsert)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## header
from components.header.header import header
app.register_blueprint(header)

## sendMailPopup
from components.sendMailPopup.sendMailPopup import sendMailPopup
app.register_blueprint(sendMailPopup)

## popup
from components.popup.popup import popup
app.register_blueprint(popup)

## insertPracticePopup
from components.insertPracticePopup.insertPracticePopup import insertPracticePopup
app.register_blueprint(insertPracticePopup)
