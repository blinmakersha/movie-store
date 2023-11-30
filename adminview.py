import flask_admin as fladmin
import flask_login as login
from flask import redirect, url_for
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView

from models import User


class MyAdminIndexView(fladmin.AdminIndexView):
    @expose('/')
    def index(self):
        """
        Authorization for '/admin' panel
        :return: redirect to '/login' if user not logged in or his role not Admin
        """
        if not login.current_user.is_authenticated:
            return redirect(url_for('login'))
        else:
            admin = User.query.filter(
                User.id == login.current_user.get_id()).first()
            if admin.role == 1:
                return super(MyAdminIndexView, self).index()
            return redirect(url_for('login'))


class MyModelView(ModelView):
    column_hide_backrefs = False

    def is_accessible(self):
        """
        This method used to check is current user is authenticated and his role is Admin
        :return:
        """
        if not login.current_user.is_authenticated:
            return False
        else:
            admin = User.query.filter(
                User.id == login.current_user.get_id()).first()
            if admin.role == 1:
                return True
            return False


class OrderView(MyModelView):
    """
    View for '/admin/order'
    """
    column_list = ('id', 'user_id', 'date', 'total')
    column_searchable_list = ('id', 'user_id')
    column_filters = ('id', 'user_id')


class MoviesView(MyModelView):
    """
    View for '/admin/movies'
    """
    column_list = ('id', 'title', 'director', 'year', 'genre', 'kind', 'duration', 'price')
    column_searchable_list = ('title', 'director')
    column_filters = ('title', 'director')
