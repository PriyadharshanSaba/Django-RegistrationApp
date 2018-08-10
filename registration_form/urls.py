from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' ,views.register, name='reg'),
    url(r'^bib_update', views.bib_update, name="update"),
    url(r'^details_pass',views.details_pass, name = "details"),
    url(r'^bib_search',views.bib_search, name = "search"),
    url(r'^exists',views.bib_exists, name = "exists"),
    url(r'^bib_edit',views.bib_edit, name = "edit"),
    url(r'^details_data',views.details_data, name = "details_pass"),


]
