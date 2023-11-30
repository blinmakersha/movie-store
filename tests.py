import os
import unittest

import pytest
from flask_login import login_user
from flask_testing import TestCase

from app import User, app, db
from models import Movies


class YourAppTestCase(TestCase):
    default_user = None

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = (f'postgresql://'
                                                 f'{os.getenv("POSTGRES_USER")}'
                                                 f':{os.getenv("POSTGRES_PASSWORD")}'
                                                 f'@localhost:'
                                                 f'{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}')
        return app

    def setUp(self):
        db.create_all()
        user = User(
        )
        db.session.add(user)
        db.session.commit()
