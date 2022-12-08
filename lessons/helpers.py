from django.conf import settings
from django.shortcuts import redirect


# A decorator that prohibits a logged in user from accessing a view
def login_prohibited(view_function):
    def modified_view_function(request):
        if request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL_WHEN_LOGGED_IN)
        else:
            return view_function(request)
    return modified_view_function


# A decorator that prohibits a logged in admin user from accessing a view
def admin_login_prohibited(view_function):
    def modified_view_function(request, **kwargs):
        if request.user.user_type == 5:
            return redirect("admin_page")
        elif request.user.user_type == 4:
            return redirect("admin_page")
        else:
            return view_function(request, **kwargs)
    return modified_view_function


# A decorator that necessitates a user to be logged in as an admin to access a view
def admin_login_required(view_function):
    def modified_view_function(request, **kwargs):
        if request.user.user_type == 5:
            return view_function(request, **kwargs)
        elif request.user.user_type == 4:
            return view_function(request, **kwargs)
        else:
            return redirect(settings.REDIRECT_URL_WHEN_LOGGED_IN)
    return modified_view_function


