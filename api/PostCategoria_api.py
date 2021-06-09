from flask_restful import Resource
from app import mysql

class PostCategoria_api(Resource):
    def get(self,id):
        cur = mysql.connection.cursor()
        cur.execute('''Select p.titulo, c.nombre as categoría
                        from `myblog-mpo`.post as p
                        left join `myblog-mpo`.categoría as c
                        on p.idcategoría =c.idcategoría
                        where p.idcategoría ='''+id)
        result = cur.fetchall()
        return str(result)