from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.konvload),
    path('', views.konvresult),
    path('', views.signupconf),
    path('konvload/', include('konvload.urls')),
    path('konvresult/', include('konvresult.urls')),
    path('signupconf/', include('signupconf.urls')),
]