import os
from flask import Flask

from project.configuration import configuration
from project.configuration.extensions import initialize_extensions
from project.frontend.controllers import register_blueprints


def create_app(config_name='develop', app_name=configuration.BaseConfig.PROJECT):
    config_obj = configuration.options(config_name)
    template_path = '{0}{1}'.format(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), config_obj.TEPLATE_PATH)
    static_path = '{0}{1}'.format(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), config_obj.STATIC_PATH)
    app = Flask(app_name, template_folder=template_path, static_folder=static_path)
    app.config.from_object(config_obj)
    register_blueprints(app)
    initialize_extensions(app)

    return app
