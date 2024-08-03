def success(data):
    return {
        'data': data,
        'errorCode': 0,
        'errorMsg': ""
    }

def args_missing():
    return {
        'data': {},
        'errorCode': 400,
        'errorMsg': "Missing argument"
    }

def data_not_exist():
    return {
        'data': {},
        'errorCode': 401,
        'errorMsg': "Data Not Exist"
    }