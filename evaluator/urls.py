from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name = "login"),
    path("home/", views.home, name = "home"),
    path("search/", views.search, name = "search"),
    path("search/results/", views.results, name = "results"),
    path("confirmation/", views.save_points, name = "save_points" ),
    path("logout/", views.signout, name = "logout" ),
    path("scores/", views.scores, name = "scores")

]