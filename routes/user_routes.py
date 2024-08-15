import json
from flask import Blueprint, jsonify, request
from sqlalchemy.orm.exc import NoResultFound
from model.db_model import Record, Users
from create_app import db
from parser.models_parser import to_dict
from parser.msg_parser import data_not_exist, success


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route("/")
def home():
    return "???"

@user_bp.route("/login", methods=['GET'])
def login():
    name = request.args.get('name')
    password = request.args.get('password')

    query = db.session.query(
        Users.uid, Users.unickname, Users.upic
    ).filter(
        Users.uname == name,
        Users.upassword == password
    ).limit(1)
    # <class 'sqlalchemy.engine.row.Row'>

    try:
        result = query.one()
        Dict = {key: value for key, value in result._asdict().items()}
        return jsonify(success(Dict))
    except NoResultFound:
        return jsonify(data_not_exist())

    

@user_bp.route("/signup")
def add_user():
    user = Users(uname="a", upassword="1234556")
    db.session.add(user)
    db.session.commit()
    return "创建成功"


@user_bp.route("/records", methods=['GET'])
def get_records():
    id = request.args.get('id')

    record_list = Record.query.filter_by(uid=id).all()
    #print(type(record_list[0]))

    result_list = []
    for record in record_list:
        dict = to_dict(record)
        dict['point']=json.loads(record.point)
        result_list.append(dict)

    return jsonify(success(result_list))
