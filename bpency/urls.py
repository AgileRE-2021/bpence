from django.urls import path

from . import views

urlpatterns = [
    # ex: / or empty
    path('', views.index, name='index'),
    # ex: /login
    # path('/login', views.login, name='login'),
    # ex: /login
    # path('/signup', views.signup, name='signup'),
]