from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

HOSTNAME = "121.41.170.185"
PORT = 3306
USERNAME = "root"
PASSWORD = "!200408Wpprpi!"
DATABASE = "travel4"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"


db = SQLAlchemy(app)