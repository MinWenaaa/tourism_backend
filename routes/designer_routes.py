from flask import Blueprint, json, request, jsonify
from intellij_designer.designer import get_resort
from intellij_designer.output import tourism_deisgner
from parser.msg_parser import args_missing, data_not_exist, success

designer_bp = Blueprint('designer', __name__)

@designer_bp.route("/chat", methods=['GET'])
def chat():
    pass
    # requirement = request.args.get('requirement')
    # id_list = get_resort(requirement,3)
    # result = []
    # for id in id_list:
    #     query = db.session.query(
    #         pois.pid, pois.pname, pois.pintroduce_short, pois.paddress, pois.pphoto,
    #         func.ST_X(pois.plocation).label('x'),
    #         func.ST_Y(pois.plocation).label('y'),
    #     ).filter_by(pid = id).first()
    #     Dict = {key: value for key, value in query._asdict().items()}
        
    #     if Dict['pphoto'] is not None:
    #         Dict['pphoto']= Dict['pphoto'][0]
    #     result.append(Dict)
    # return jsonify(success(result))


@designer_bp.route("/designer", methods=['POST'])
def test():
    pass
    # print("start")
    # data = request.get_json()
    # requirement = data['requirement']
    # num = data['num']

    # print(requirement)

    # if not requirement:
    #     return jsonify(args_missing)
    
    # id_list = tourism_deisgner(requirement, num*5)

    # result_list = []
    # for i in range(0, int(num)):
    #     temp = []
    #     for j in range(0,3):
    #         query = db.session.query(
    #             pois.pid, pois.pname, pois.pintroduce_short, pois.paddress, pois.pphoto,
    #             func.ST_X(pois.plocation).label('x'),
    #             func.ST_Y(pois.plocation).label('y'),
    #         ).filter_by(pid = id_list[i*3+j]).first()
    #         Dict = {key: value for key, value in query._asdict().items()}
        
    #         if Dict['pphoto'] is not None:
    #             Dict['pphoto']= Dict['pphoto'][0]
    #         temp.append(Dict)
    #     result_list.append(temp)

    # print(success(result_list))
    
    # return jsonify(success(result_list))


@designer_bp.route("/getItiData", methods=['GET'])
def getItiData():
    pass
    # id = request.args.get('id')
    # POI = db.session.query(
    #         pois.pid, pois.pname, pois.pintroduce_short, pois.paddress, pois.pphoto,
    #         func.ST_X(pois.plocation).label('x'),
    #         func.ST_Y(pois.plocation).label('y'),
    #     ).filter_by(pid=id).first()
    # Dict = {key: value for key, value in POI._asdict().items()}
    # if Dict['pphoto'] is not None:
    #     Dict['pphoto']= Dict['pphoto'][0]
    # return jsonify(success(Dict))


@designer_bp.route("/push_plan", methods = ['POST'])
def push_plan():
    pass
    # data = request.get_json()
    # name = data['name']
    # itidata = data['itidata']
    # uid = data['uid']
    # pic = data['pic']
    # print(pic)
    # id = data['id']
    # edittime = data['edittime']

    # if not id:
    #     plan = Plan(name=name, itidata=itidata, uid=uid, pic=pic, edittime=edittime)
    #     db.session.add(plan)
    
    # else:
    #     plan = Plan.query.get(id)

    #     plan.name = name
    #     plan.itidata = itidata
    #     plan.pic = pic
    #     plan.edittime = edittime

    # try:
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({"error": str(e)}), 500
    
    # print(plan.pic)

    # return jsonify(success({"id": plan.id}))
    

@designer_bp.route("/read_plan", methods =['get'])
def read_plan():
    pass
    # id = request.args.get('id')

    # if not id:
    #     return jsonify(args_missing)
    
    # id = int(id)
    # plan = Plan.query.filter_by(id=id).first()

    # if not plan:
    #     return jsonify(data_not_exist())
    
    # result = detail_item(plan)


    # return jsonify(success(result))




@designer_bp.route("/plans", methods = ['GET'])
def get_plans():
    pass
    # id = request.args.get('id')

    # query = db.session.query(
    #     Plan.name, Plan.pic, Plan.edittime, Plan.id
    # ).filter_by(uid=id).all()
    # #print(type(record_list[0]))

    # result_list = []
    # for record in query:
    #     Dict = {key: value for key, value in record._asdict().items()}
    #     result_list.append(Dict)

    # return jsonify(success(result_list))
