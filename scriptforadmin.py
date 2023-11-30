from werkzeug.security import generate_password_hash

from app import app, db
from models import User

new_user = User(name="admin", email="admin@gmail.com",
                password=generate_password_hash("admin"), role=1)

with app.app_context():
    db.session.add(new_user)
    db.session.commit()
