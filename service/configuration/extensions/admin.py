from flask_admin import Admin
from flask_admin.base import MenuLink
from project.models import User, Role
from project.frontend.controllers.admin import UserAdminView, RoleAdminView
from project.configuration.extensions import sqldb
from project.frontend.controllers.admin import IndexAdminView


def configure_admin(app):
    admin = Admin(index_view=IndexAdminView(endpoint='admin'))
    admin.init_app(app)
    admin.add_link(MenuLink(name='Logout', url='/user/logout'))
    admin.add_view(UserAdminView(User, sqldb.session, endpoint='user-admin'))
    admin.add_view(RoleAdminView(Role, sqldb.session, endpoint="role-admin"))

    return app
