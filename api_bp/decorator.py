from functools import wraps

import jwt
from flask import current_app, request
from werkzeug.security import check_password_hash

from models import User


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" in request.headers:
            token = request.headers.get("Authorization")
            if token:
                try:
                    data = jwt.decode(token, current_app.secret_key, algorithms=[
                                      "HS256"])
                    user = User.query.filter(
                        User.email == data["email"]).first()
                    if not user:
                        return {"message": "user not found"}, 401
                    if not check_password_hash(user.password, data["password"]):
                        return {"message": "password invalid"}, 401

                except Exception as e:
                    return {"message": "Invalid token", "error": str(e)}, 401
            else:
                return {"message": "Authentication token required"}, 401
        else:
            return {"message": "Authorization required"}, 401

        return func(*args, **kwargs)

    return wrapper
