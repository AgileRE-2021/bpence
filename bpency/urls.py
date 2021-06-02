from django.urls import path

from . import views

urlpatterns = [
    # ex: / or empty
    path('', views.index, name='index'),
    # ex: /login
    path('login', views.login_view, name='login'),
    # ex: /signup
    path('signup', views.signup_view, name='signup'),
    # ex: /konversi
    path('konversi', views.konversi, name='konversi'),
]
