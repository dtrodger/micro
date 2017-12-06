from login import login_manager
from mail import mail_api
from sqldb import sqldb
from bcrypt_api import bcrypt
from debug_toolbar import debug_toolbar
from js_glue import jsglue
from upload import configure_uploads, file
from csrf import csrf
from security import user_datastore, security
# from scheduler import scheduler
from admin import configure_admin


def initialize_extensions(app):
    sqldb.init_app(app)
    login_manager.init_app(app)
    mail_api.init_app(app)
    bcrypt.init_app(app)
    debug_toolbar.init_app(app)
    jsglue.init_app(app)
    configure_uploads(app, file)
    csrf.init_app(app)
    configure_admin(app)
    security.init_app(app, user_datastore)
    # scheduler.init_app(app)
    # scheduler.start()
    # app.extensions['scheduler'] = scheduler

    return app
