from flask_restful import Resource, request
from basic.create_sql import User
from flask import jsonify
import sqlite3


user = User()


class __CreateUser(Resource):
    def post(self):
        try:
            user.add_user(
                username=request.json['username'],
                email=request.json['email'],
                password=request.json['password'],
                biografia=request.json['biografia'],
                photoURL=request.json['photoURL'],
                idiomas=request.json['idiomas'],
                name=request.json['name'],
            )
            return jsonify(
                message="User created"
            )
        
        except sqlite3.IntegrityError:
            return jsonify(
                message="Dados incorretamente preenchidos"
            )

        except Exception as e:
            print(e)
            return jsonify(
                message="Deu erro"
            )
        
