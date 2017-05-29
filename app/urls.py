from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^TipoUsuario/', views.TipoUsuario, name='TipoUsuario'),
    url(r'^registrarFijo/', views.registrarFijo, name='registrarFijo'),
    url(r'^registrarAmbulante/', views.registrarAmbulante, name='registrarAmbulante'),
    url(r'^registrarAlumno/', views.registrarAlumno, name='registrarAlumno'),
    url(r'^registrarProducto/(?P<id>[0-9]+)$', views.registrarProducto, name='registrarProducto'),
    url(r'^gestionproductos/(?P<id>[0-9]+)$', views.gestionproductos, name='gestionproductos'),
    url(r'^vendedorprofilepage/(?P<id>[0-9]+)$', views.vendedorprofilepage, name='vendedorprofilepage'),
    url(r'^editarvendedor/(?P<id>[0-9]+)$', views.editar_vendedor, name='editarvendedor'),
    url(r'^$', views.index, name='index'),
]