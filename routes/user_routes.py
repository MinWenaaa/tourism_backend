import json
import os
from flask import Blueprint, jsonify, request, send_from_directory
#from sqlalchemy.orm.exc import NoResultFound
#from model.db_model import Event, Record, Users
from parser.msg_parser import success, args_missing, data_not_exist
from create_app import connection
from mysql.connector import Error

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route("/")
def home():
    return "???"

    
    
@user_bp.route("/login", methods=['GET'])
def login():
    username = request.args.get('name')
    password = request.args.get('password')
    if not username or not password:
        return jsonify({"success": False, "message": "Username and password are required"}), 400
    if not connection:
        return jsonify({"success": False, "message": "Database connection error"}), 502
    try:
        cursor = connection.cursor(dictionary=True) 
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            return jsonify(success(user))
        else:
            return jsonify({"success": False, "message": "Invalid username or password"}), 401

    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 501
    finally:
        if connection.is_connected():
            cursor.close()
            #connection.close()
    return f"${name}, ${password}"

    # query = db.session.query(
    #     Users.uid, Users.unickname, Users.upic
    # ).filter(
    #     Users.uname == name,
    #     Users.upassword == password
    # ).limit(1)
    # <class 'sqlalchemy.engine.row.Row'>

    # try:
    #     result = query.one()
    #     Dict = {key: value for key, value in result._asdict().items()}
    #     return jsonify(success(Dict))
    # except NoResultFound:
    #     return jsonify(data_not_exist())

    

@user_bp.route("/signup")
def add_user():
    pass
    # user = Users(uname="a", upassword="1234556")
    # db.session.add(user)
    # db.session.commit()
    # return "创建成功"


@user_bp.route("/create_record", methods=['POST'])
def create_record():
    pass
    # data = request.get_json()
    # print(data)
    # id = data['id']
    # point = data['start']
    # name = data['name']
    # print(name)

    # record = Record(uid = id, point = [point], name=name)
    # print(record.name)

    # db.session.add(record)
    # db.session.commit()

    # return jsonify(success({"id": record.id}))



@user_bp.route("/records", methods=['GET'])
def get_records():
    pass
    # id = request.args.get('id')

    # record_list =  db.session.query(
    #     Record.id, Record.name,
    # ).filter_by(uid=id).all()
    # #print(type(record_list[0]))

    # result_list = []
    # for record in record_list:
    #     Dict = {key: value for key, value in record._asdict().items()}
    #     print(dict)

    #     result_list.append(Dict)

    # print(result_list)
    # return jsonify(success(result_list))

@user_bp.route("/recordDetail", methods=['GET'])
def get_record_detail():
    pass
    # id = request.args.get('id')

    # record = Record.query.filter_by(id=id).first()


    # query = Event.query.filter_by(rid=id).all()

    # event_list = []
    # for event in query:
    #     Dict = to_dict(event)
    #     event_list.append(Dict)
    # #print(type(result), type(event_list))

    # result = {"points": json.loads(record.point),
    #           "events": event_list},

    # return jsonify(success(result))



@user_bp.route("/push_point", methods=['POST'])
def push_point():
    pass
    # data = request.get_json()
    # id = data['id']
    # print(id)
    # newPoint = data['point']

    # record = Record.query.get(id)
    # if not isinstance(record.point, list):
    #     if isinstance(record.point, str):
    #         record.point = json.loads(record.point)
    #     else:
    #         record.point = [] 
    
    # #print(record.point)
    # record.point.append(newPoint)
    # record.point = json.dumps(record.point)
    # #print(record.point)
    # try:
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({"error": str(e)}), 500
    # return jsonify(success({}))


@user_bp.route('/insertEvent', methods=['POST'])
def upload_image():
 
    if 'file' not in request.files:
        return jsonify(args_missing())
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify(args_missing())
    
    if file:
        rid = request.form.get('id')
        point = request.form.get('point')
        text = request.form.get('text')

        event = Event(rid=rid, point=point, text=text)
        db.session.add(event)
        db.session.commit()

        id = event.id
        
        filename = str(id)+".jpg"
        file.save(os.path.join('C:\\photos', filename))
        
        return jsonify(success({'id':id}))
    

@user_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:

        return send_from_directory(directory='C:\\photos',
                                   path=filename,
                                   as_attachment=True)  # 设置为附件，以便下载
    except FileNotFoundError:
        return jsonify