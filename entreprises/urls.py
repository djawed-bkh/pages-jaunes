from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entreprises_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^recherche', views.recherche, name='recherche'),
    url(r'^inscription', views.inscription, name='inscription'),
    url(r'^conexion', views.conexion, name='conexion'),
     url(r'^infos', views.infos, name='infos'),
    # ex: /polls/5/
]