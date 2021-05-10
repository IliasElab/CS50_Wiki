from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.create, name="create"),
    path("chance", views.chance, name="chance"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry")
]
