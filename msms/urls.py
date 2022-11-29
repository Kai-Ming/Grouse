"""msms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lessons import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('admin/', admin.site.urls),
    path('student_sign_up/', views.student_sign_up, name='student_sign_up'),
    path('teacher_sign_up/', views.teacher_sign_up, name='teacher_sign_up'),
    path('adult_sign_up/', views.adult_sign_up, name='adult_sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('user_page/', views.user_page, name='user_page'),
]
