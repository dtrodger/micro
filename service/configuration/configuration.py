import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    PROJECT = "Prometheus"
    SECRET_KEY = 'Gaea runs'
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    LOGIN_DISABLED=False
    TESTING = True
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    DEBUG_TB_ENABLED = False
    SECRET_KEY = None
    SECURITY_PASSWORD_SALT = None
    STRIPE_SECRET_KEY = None
    STRIPE_PUBLISHABLE_KEY = None
    SQLALCHEMY_DATABASE_URI = None

def options(option):
    return {
        "base": BaseConfig,
        "develop": DevelopmentConfig,
        "test": TestingConfig,
        "prod": ProductionConfig,
    }[option]
