from .models import User

def admin_rights_check(user):
    if (User) (user).user_type == 4 or (User) (user).user_type == 5:
        return True
    else: 
        return False

