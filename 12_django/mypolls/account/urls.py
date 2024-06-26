# account/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from . import views

app_name = "account"
urlpatterns = [
    path("join", views.create, name="join"),
    # path("login", views.user_login, name="login"),
    path("login", 
        LoginView.as_view(
            template_name="account/login.html", # login form template
            form_class=AuthenticationForm       # Form class
        ),
        name="login"),
    path("logout", views.user_logout, name="logout"),
]
# http://ip:port/account/join  -> views.create