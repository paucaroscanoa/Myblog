from flask import Flask
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)

from api.Categoria_api import Categoria_api
from api.Post_api import Post_api
from api.PostCategoria_api import PostCategoria_api
from api.hello_api import HelloWorld

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Mario4190&$"
app.config["MYSQL_DB"] = "myblog-mpo"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

api.add_resource(HelloWorld,'/hello')
api.add_resource(Categoria_api,'/categoría')
api.add_resource(Post_api,'/Post')
api.add_resource(PostCategoria_api,'/categoria/<id>/post')