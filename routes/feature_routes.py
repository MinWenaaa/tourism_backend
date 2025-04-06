from flask import Blueprint, request, jsonify

from parser.msg_parser import success, args_missing, data_not_exist

feature_bp = Blueprint('feature', __name__)

@feature_bp.route('/homepage', methods=['GET'])
def get_items():
    pass
    # type = request.args.get('type')
    # i = request.args.get('i')

    # if not (type and i):
    #     return jsonify(args_missing())
    
    # i=int(i)
    
    # a = 20*i;
    # b = a-20

    # POIs = pois.query.filter_by(ptype=type).slice(b, a).all()
    # pois_list = [poi_list_view_item(poi) for poi in POIs]

    # return jsonify(success(pois_list))

@feature_bp.route('/mapview', methods=['GET'])
def get_item():
    pass
    # id = request.args.get('id')
    # POI = pois.query.filter_by(pid=id).first()
    # return jsonify(success(poi_list_view_item(POI)))

@feature_bp.route('/detail', methods=['GET'])
def fuzzy_search():
    pass
    # id = request.args.get('id')

    # if not id:
    #     return jsonify(args_missing)
    
    # id = int(id)
    # poi = pois.query.filter_by(pid=id).first()

    # if not poi:
    #     return jsonify(data_not_exist())
    
    # result = detail_item(poi)

    # query = db.session.query(
    #     func.ST_X(pois.plocation).label('x'),
    #     func.ST_Y(pois.plocation).label('y'),
    # ).filter_by(pid=id).first()
    # coordination = {key: value for key, value in query._asdict().items()}

    # result['plocation'] = coordination

    # return jsonify(success(result))


@feature_bp.route('/comments', methods=['GET'])
def get_poi_comment():
    pass
    # id = request.args.get('id')
    # if not id:
    #     return jsonify(args_missing)
    
    # id = int(id)
    # comments_list = Comments.query.filter_by(cpid=id).all()
    # print(type(comments_list[0]))

    # result = [detail_item(com) for com in comments_list]
    # return jsonify(success(result))



@feature_bp.route('/search', methods=['GET'])
def get_item_Detail():
    pass
    # search_keyWord = request.args.get('name')
    # type = request.args.get('type')

    # if not search_keyWord:
    #     return jsonify(args_missing)

    # query = db.session.query(
    #     pois.pname, pois.pintroduce_short, pois.paddress,
    #     func.ST_X(pois.plocation).label('x'),
    #     func.ST_Y(pois.plocation).label('y'),
    # ).filter(
    #     pois.ptype == type,
    #     pois.pname.like(f'%{search_keyWord}%')
    # ).limit(5).all()
    
    # result = [];

    # for item in query:
    #     Dict = {key: value for key, value in item._asdict().items()}
    #     result.append(Dict)


    # return jsonify(success(result))