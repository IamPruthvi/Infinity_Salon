from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='main'),
    path("about", views.about, name='about'),
    path("contact_us", views.contact_us, name='contact_us'),
    path("services", views.services, name='services'),
]
