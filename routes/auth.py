import jwt
from flask import Blueprint, request, jsonify
from api.model_jwt import write_token, validate_token


routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    if data['username'] == "Raul1985":
        return write_token(data = request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response


@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    print(token)
    return validate_token(token, output = True)
