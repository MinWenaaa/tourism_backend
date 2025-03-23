from flask import Flask
import mysql.connector

app = Flask(__name__)
connection = mysql.connector.connect(
    username = 'root',
    password = '20040229w',
    host = 'localhost',
    database = 'new_schema'
)
