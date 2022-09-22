from unicodedata import name
from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path("", views.forms22, name='article')
]