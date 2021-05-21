from django.urls import path

from . import views

urlpatterns = [
    # ex: / or empty
    path('', views.index, name='index'),
    # ex: /login
    path('login', views.nav, name='login'),
    # ex: /konversi
    path('konversi', views.konversi, name='konversi'),
]