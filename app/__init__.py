from flask import Flask
from flask_mail import Mail

app = Flask(__name__)


app.config['SECRET_KEY']='cram_md5'
app.config['MAIL_SERVER']='	smtp.mailtrap.io'
app.config['MAIL_PORT']='2525'
app.config['MAIL_USERNAME']='1a262e922edc70'
app.config['MAIL_PASSWORD']='f1d4ff62cf1e1c'

mail=Mail(app)
from app import views