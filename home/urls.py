from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html")),
    path('contact/',views.contact)
]
