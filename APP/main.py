from APP import app, login_manager
from APP.models.user_model import User

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)