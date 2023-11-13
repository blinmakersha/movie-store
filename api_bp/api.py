from datetime import datetime, timedelta, timezone

import jwt
from flask import Blueprint, abort, current_app, jsonify, request

from models import Movies, User

from .decorator import token_required

api_bp = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static")


@api_bp.route('/')
def api_index():
    return jsonify({"status": 200})


@api_bp.route('/get_movies')
@token_required
def get_movies():
    movies = Movies.query.all()
    result = {}
    for movie in movies:
        result[movie.id] = {"name": movie.title,
                            "price": movie.price}
    return jsonify({"movies": result})


@api_bp.route('/get_user', methods=["GET", "POST"])
@token_required
def get_user():
    if request.method == "POST":
        user_id = request.json.get("id")
        user = User.query.filter(User.id == user_id).first()
        result = {
            user.id: {
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "orders": [order.id for order in user.orders]
            }
        }
        return jsonify(result)
    return abort(405)


@api_bp.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        exp = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        token = jwt.encode(dict(email=email, password=password,
                           exp=exp), current_app.secret_key, algorithm="HS256")
        return {"status": "token generated successfully", "token": token}
    return abort(405)
