from django.urls import path

from . import views

urlpatterns = [
    # ex: / or empty
    path('', views.index, name='index'),
    # ex: /login
    path('login', views.login, name='login'),
    # ex: /signup
    path('signup', views.signup, name='signup'),
    # ex: /konversi
    path('konversi', views.konversi, name='konversi'),

    path('jajal', views.jajal, name='jajal'),
]
