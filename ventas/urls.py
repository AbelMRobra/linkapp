from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^estmerc$', views.estmercado, name = 'Estudio de mercado'),

]