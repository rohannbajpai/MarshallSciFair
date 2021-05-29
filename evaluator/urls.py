from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name = "login"),
    path("home/", views.home, name = "home"),
    path("home/search", views.search, name = "search"),
    path("home/confirmation", views.save_points, name = "save_points" ),
    path("logout/", views.signout, name = "logout" )

]