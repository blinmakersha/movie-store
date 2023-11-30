import os
import unittest

import pytest
from flask_login import login_user
from flask_testing import TestCase

from app import User, app, db
from models import Movies, Order


class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        self.app = app
        return self.app

    def test_home(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_films(self):
        response = self.client.get('/films')
        self.assertEqual(response.status_code, 200)

    def test_tvseries(self):
        response = self.client.get('/tvseries')
        self.assertEqual(response.status_code, 200)

    def test_cartoons(self):
        response = self.client.get('/cartoons')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        user = User(name="test", email="test@test.com",
                    password="test", role=2)
        db.session.add(user)
        db.session.commit()
        query_user = User.query.filter_by(email="test@test.com").first()
        self.assertEqual(query_user.name, "test")

    def test_auth(self):
        self.app.post(
            '/login', data={'email': 'test@test.com', 'password': 'test'})
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_logout_route(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
