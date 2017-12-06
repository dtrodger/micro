import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from flask_script import Manager, Shell, Server

from project import create_app
from project.utilities.shell_context import _make_context

app = create_app()

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("server", Server(use_reloader=True))

if __name__ == '__main__':
    from manager.commands import add_commands
    add_commands(manager)
    manager.run()
