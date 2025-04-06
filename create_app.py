from flask import Flask
import mysql.connector

app = Flask(__name__)
# connection = mysql.connector.connect(
#     user = 'root',
#     password = '20040229w',
#     host = 'localhost',
#     database = 'new_schema'
# )

try:
    # 建立连接
    connection = mysql.connector.connect(
        user = 'root',
        password = '20040229w',
        host = 'localhost',
        database = 'new_schema'
    )

    # 检查连接是否成功
    if connection.is_connected():
        print("连接成功！")
        # 获取数据库版本信息
        db_info = connection.get_server_info()
        print("MySQL 数据库版本：", db_info)
    else:
        print("连接失败！")
except Error as e:
    print("连接失败，错误信息：", e)
finally :
    pass