from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    url(r'^documentacion$', login_required(views.documentacion), name = 'Documentacion'),


    ######## ----------------> Gerenciador
    url(r'^gerenpanel$', login_required(views.gerenciamientopanel), name = 'Panel del gerenciador'),
    url(r'^gerenproyecto/(?P<id_proyecto>\d+)/$', login_required(views.gerenciamientoproyecto), name = 'Gerenciador - Proyecto'),



    ######## ----------------> Registros de desvios

    url(r'^registrospanel$', login_required(views.registrodesvios), name = 'Registros de desvios'),
    url(r'^registrosid/(?P<id_registro>\d+)/$', login_required(views.registrodesviosid), name = 'Registros ID'),

    url(r'^principaltecnica$', login_required(views.principaltecnica), name = 'Principal Tecnica'),
    url(r'^documentacionamp/(?P<id_proyecto>\d+)/(?P<id_estado>\d+)/(?P<id_week>\d+)/$', login_required(views.documentacionamp), name = 'Documentacion Amp'),
    url(r'^editaritem/(?P<id_item>\d+)/$', login_required(views.editaritem), name = 'Editar Item'),
    url(r'^editarsubitem/(?P<id_subitem>\d+)/$', login_required(views.editarsubitem), name = 'Editar subitem'),  
    url(r'^editarsubsubitem/(?P<id_subsubitem>\d+)/$', login_required(views.editarsubsubitem), name = 'Editar subsubitem'),  
    url(r'^eliminaritem/(?P<id_item>\d+)/$', login_required(views.eliminaritem), name = 'Borrar Item'), 
    url(r'^agregaritem/(?P<id_etapa>\d+)/$', login_required(views.agregaritem), name = 'Agregar Item'), 
    url(r'^gantt/(?P<id_proyecto>\d+)/$', login_required(views.ganttet), name = 'Gantt ET'), 
    url(r'^mensajeitem/(?P<id_item>\d+)/$', login_required(views.mensajesitem), name = 'Mensaje item'),
    url(r'^bbddgroup/$', login_required(views.bbddgroup), name = 'BBDD group'), 
    url(r'^agregarsubitem/(?P<id_item>\d+)/$', login_required(views.agregarsubitem), name = 'Agregar Subitem'),
    url(r'^agregarsubsubitem/(?P<id_subitem>\d+)/$', login_required(views.agregarsubsubitem), name = 'Agregar Subsubitem'), 

]