from flask_security import SQLAlchemyUserDatastore, Security
from sqldb import sqldb
from project.models import User, Role

user_datastore = SQLAlchemyUserDatastore(sqldb, User, Role)
security = Security()
