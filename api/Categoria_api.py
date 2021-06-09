from flask_restful import Resource
from app import mysql


class Categoria_api(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("Select*from categoría")
        result=cur.fetchall()
        return str(result)