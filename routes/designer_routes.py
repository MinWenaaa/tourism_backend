from flask import Blueprint, request, jsonify
from intellij_designer.output import tourism_deisgner
from parser.msg_parser import args_missing

designer_bp = Blueprint('designer', __name__)

@designer_bp.route("/", methods=['GET'])
def test():
    requirement = request.args.get('requirement')

    if not requirement:
        return jsonify(args_missing)
    
    return jsonify(tourism_deisgner(requirement))