from flask_restful import Resource
from app import mysql

class Post_api(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("Select * from Post")
        result=cur.fetchall()
        return str(result)