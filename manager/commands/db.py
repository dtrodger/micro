import sys
import os
import itertools
from random import randint
from faker import Faker
from flask_script import Command

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from project.middleware import UserApi
from project.configuration.extensions import sqldb
from project.models import User


class ResetSQLDB(Command):
    def run(self):
        print 'Resetting SQL DB...'
        sqldb.drop_everything()
        sqldb.create_all()


class DropSQLDB(Command):
    def run(self):
        print 'Dropping SQL DB...'
        sqldb.drop_everything()


class BootstrapDatabase(Command):
    def __init__(self, *args):
        super(self.__class__, self).__init__(*args)

    def run(self):
        print 'Bootstraping database...'
