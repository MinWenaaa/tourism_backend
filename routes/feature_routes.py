from flask import Blueprint, request, jsonify
from sqlalchemy.sql import func
from models.db_model import pois
from parser.models_parser import poi_list_view_item, poi_detail_item
from parser.msg_parser import success, args_missing, data_not_exist
from create_app import db

feature_bp = Blueprint('feature', __name__)

@feature_bp.route('/homepage', methods=['GET'])
def get_items():
    type = request.args.get('type')
    i = request.args.get('i')

    if not (type and i):
        return jsonify(args_missing())
    
    i=int(i)
    
    a = 20*i;
    b = a-20

    POIs = pois.query.filter_by(ptype=type).slice(b, a).all()
    pois_list = [poi_list_view_item(poi) for poi in POIs]

    return jsonify(success(pois_list))


@feature_bp.route('/detail', methods=['GET'])
def get_item_Detail():
    id = request.args.get('id')

    if not id:
        return jsonify(args_missing)
    
    id = int(id)
    poi = pois.query.filter_by(pid=id).first()

    if not poi:
        return jsonify(data_not_exist())
    
    result = poi_detail_item(poi)

    query = db.session.query(
        func.ST_X(pois.plocation).label('x'),
        func.ST_Y(pois.plocation).label('y'),
    ).filter_by(pid=id).first()
    coordination = {key: value for key, value in query._asdict().items()}

    result['plocation'] = coordination

    return jsonify(success(result))
