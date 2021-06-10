from flask_restful import Resource
from flask import jsonify
from app import mysql

class Post_api(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("Select * from Post")
        result=cur.fetchall()
        return jsonify(result) # jsonify combierte a formato jason