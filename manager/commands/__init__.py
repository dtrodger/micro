from db import *


def add_commands(manager):
    manager.add_command('reset_sqldb', ResetSQLDB())
    manager.add_command('drop_sqldb', DropSQLDB())
    manager.add_command('delete_users', DeleteUser())
    return manager
