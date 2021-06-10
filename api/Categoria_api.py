from flask_restful import Resource
from flask import jsonify
from app import mysql

class Categoria_api(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("Select*from categoría")
        result=cur.fetchall()
        return jsonify(result) # jsonify combierte a formato jason