from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"
