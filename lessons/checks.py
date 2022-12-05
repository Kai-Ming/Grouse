from .models import User

def admin_rights_check(user):
    if (User) (user).user_type == 4 or (User) (user).user_type == 5:
        return True
    else: 
        return False

def not_a_student_check(user):
    if (User) (user).user_type == 1:
        return False
    else: 
        return True

