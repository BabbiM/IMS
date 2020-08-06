
from django.conf.urls import include,url
from django.contrib import admin

#from . import views
from sims import views
urlpatterns = [
    url(r'^$', views.about, name='about'),
   # url(r'^', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^create', views.create, name='create'),
    url(r'^send', views.send, name='send'),
    url(r'^closed', views.closed, name='closed'),
    url(r'^escalated', views.escalate, name='escalated'),
    url(r'^assign', views.assign, name='assign'),
    url(r'^about', views.about, name='about'),
    url(r'^index', views.index, name='index'),
    #url(r'^video', views.index, name='video'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts', include('django.contrib.auth.urls')),
    url(r'^send_incident', views.send_incident, name='send_incident'),
    #url(r'^snippet', views.snippet_detail, name='snippet')
    #path('snippet',views.snippet_detail)
]