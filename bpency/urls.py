from django.urls import path

from . import views

urlpatterns = [
    # ex: / or empty
    path('', views.index, name='index'),
    # ex: /logged
    path('logged', views.indexacc, name='index akun'),

    # ex: /login
    path('login', views.login, name='login'),
    # ex: /signup
    path('signup', views.signup, name='signup'),
    # ex: /konversi
    path('konversi', views.konversi, name='konversi'),
    # ex: /konversi-load
    path('konversi-load', views.konvload, name='loading_konversi'),
    # ex: /history
    path('history', views.histori, name='histori'),
    # ex: /hasil
    path('hasil', views.hasil, name='hasil'),
]
