from sqlalchemy import inspect
import json

def poi_list_view_item(poi):
    photo = None
    if poi.pphoto is not None:
        photo = poi.pphoto[0]
    return {
        'pid': poi.pid,
        'pname': poi.pname,
        'pclass': poi.pclass,
        'paddress': poi.paddress,
        'pphoto': photo,
        'pgrade': poi.pgrade,
        'plevel': poi.plevel,
        'pprice': poi.pprice,
        'pintroduce_short': poi.pintroduce_short,
        'popen_time': poi.popen_time,
        'pphonenumber': poi.pphonenumber,
        'precommended_duration': poi.precommended_duration,
        'prank': poi.prank
    }

def detail_item(poi):
    model_dict = {}
    
    model_columns = [c_attr.key for c_attr in inspect(poi).mapper.column_attrs]
    
    # Iterate over each column and add it to the dictionary
    for column in model_columns:
        value = getattr(poi, column)
        
        # For JSON fields, get the actual value
        if isinstance(value, dict):
            model_dict[column] = value
        else:
            model_dict[column] = value
    
    return model_dict

