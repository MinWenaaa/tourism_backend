from flask import Blueprint, json, request, jsonify
from sqlalchemy import func
from intellij_designer.output import tourism_deisgner
from model.db_model import Plan, Record, pois
from create_app import db
from parser.models_parser import detail_item
from parser.msg_parser import args_missing, data_not_exist, success

designer_bp = Blueprint('designer', __name__)

@designer_bp.route("/designer", methods=['POST'])
def test():
    print("start")
    data = request.get_json()
    requirement = data['requirement']
    num = data['num']

    print(requirement)

    if not requirement:
        return jsonify(args_missing)
    
    id_list = tourism_deisgner(requirement, num)

    result_list = []
    for i in range(0, int(num)//3):
        temp = []
        for j in range(0,3):
            query = db.session.query(
                pois.pid, pois.pname, pois.pintroduce_short, pois.paddress, pois.pphoto,
                func.ST_X(pois.plocation).label('x'),
                func.ST_Y(pois.plocation).label('y'),
            ).filter_by(pid = id_list[i*3+j]).first()
            Dict = {key: value for key, value in query._asdict().items()}
        
            if Dict['pphoto'] is not None:
                Dict['pphoto']= Dict['pphoto'][0]
            temp.append(Dict)
        result_list.append(temp)

    print(success(result_list))
    
    return jsonify(success(result_list))



@designer_bp.route("/push_plan", methods = ['POST'])
def push_plan():
    data = request.get_json()
    name = data['name']
    itidata = data['itidata']
    uid = data['uid']
    pic = data['pic']
    edittime = data['edittime']

    plan = Plan(name=name, itidata=itidata, uid=uid, pic=pic, edittime=edittime)
    db.session.add(plan)
    db.session.commit()

    return jsonify(success({"id": plan.id}))
    

@designer_bp.route("/read_plan", methods =['get'])
def read_plan():

    id = request.args.get('id')

    if not id:
        return jsonify(args_missing)
    
    id = int(id)
    plan = Plan.query.filter_by(id=id).first()

    if not plan:
        return jsonify(data_not_exist())
    
    result = detail_item(plan)


    return jsonify(success(result))




@designer_bp.route("/plans", methods = ['GET'])
def get_plans():
    id = request.args.get('id')

    query = db.session.query(
        Plan.name, Plan.pic, Plan.edittime, Plan.id
    ).filter_by(uid=id).all()
    #print(type(record_list[0]))

    result_list = []
    for record in query:
        Dict = {key: value for key, value in record._asdict().items()}
        result_list.append(Dict)

    return jsonify(success(result_list))


@designer_bp.route("/plan_refresh", methods = ['POST'])
def refresh():
    

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