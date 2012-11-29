from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^subir_fichero/$', 'caja.views.subir_fichero', name='subir_fichero'),
)
