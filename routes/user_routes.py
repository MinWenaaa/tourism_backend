from flask import Blueprint
from models.db_model import Users
from create_app import db


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route("/")
def home():
    return "???"

@user_bp.route("/add")
def add_user():
    user = Users(uname="a", upassword="1234556")
    db.session.add(user)
    db.session.commit()
    return "创建成功"