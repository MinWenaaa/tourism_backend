from flask import Blueprint, json, request, jsonify
from sqlalchemy import func
from intellij_designer.output import tourism_deisgner
from model.db_model import Record, pois
from create_app import db
from parser.msg_parser import args_missing, success

designer_bp = Blueprint('designer', __name__)

@designer_bp.route("/", methods=['POST'])
def test():

    data = request.get_json()
    requirement = data['requirement']
    num = data['num']

    if not requirement:
        return jsonify(args_missing)
    
    id_list = tourism_deisgner(requirement, num)

    result_list = []
    for id in id_list:
        query = db.session.query(
            pois.pid, pois.pname, pois.pintroduce_short, pois.paddress, pois.pphoto,
            func.ST_X(pois.plocation).label('x'),
            func.ST_Y(pois.plocation).label('y'),
        ).filter_by(pid = id).first()
        Dict = {key: value for key, value in query._asdict().items()}
        
        if Dict.pphoto is not None:
            Dict.pphoto = Dict.pphoto.pphoto[0]
        result_list.append(Dict)
    
    return jsonify(success(result_list))



@designer_bp.route("/create_record", methods=['POST'])
def create_record():

    data = request.get_json()
    print(data)
    id = data['id']
    point = data['start']
    name = data['name']
    print(name)

    record = Record(uid = id, point = [point], name=name)
    print(record.name)

    db.session.add(record)
    db.session.commit()

    return jsonify(success({"id": record.id}))



@designer_bp.route("/push_point", methods=['POST'])
def push_point():

    data = request.get_json()
    id = data['id']
    newPoint = data['point']

    record = Record.query.get(id)
    if not isinstance(record.point, list):
        if isinstance(record.point, str):
            record.point = json.loads(record.point)
        else:
            record.point = [] 
    print(record.point)
    record.point.append(newPoint)
    record.point = json.dumps(record.point)
    print(record.point)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    return jsonify(success({}))


"""
@designer_bp.route("/upload_photo", methos=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        new_image = Image(filename=filename)
        db.session.add(new_image)
        db.session.commit()
        return f"File {filename} uploaded successfully", 201
"""