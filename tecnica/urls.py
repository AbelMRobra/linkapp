from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    url(r'^documentacion$', login_required(views.documentacion), name = 'Documentacion'), 

]