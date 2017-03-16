from django.conf.urls import patterns, include, url
from django.contrib import admin
import calc.views
urlpatterns = patterns('',
    
    url(r'(\d+)\+(\d+)', calc.views.suma, name="sumar"),
    url(r'(\d+)\-(\d+)', calc.views.resta, name="restar"),
    url(r'(\d+)\*(\d+)', calc.views.multiplica, name="multiplicar"),
    url(r'(\d+)/(\d+)', calc.views.divide, name="dividir"),
    url(r'^admin/', include(admin.site.urls)),
)
