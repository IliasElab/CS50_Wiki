from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.create, name="create"),
    path("chance", views.chance, name="chance"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('encyclopedia/favicon.ico')))
]
