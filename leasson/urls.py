from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'leasson'

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createleasson/', views.createleasson, name='createleasson'),
    url(r'^leassondeatil/(?P<id>\d+)/$', views.leassondeatil, name='leassondeatil'),
    url(r'^accecptleasson/', views.MyJob, name='MyJob'),
    url(r'^my_leasson/', views.my_leasson, name='my_leasson'),
    url(r'^leasson_delete/(?P<slug>[-\w]+)/$', views.leasson_delete, name='leasson_delete'),
    url(r'^accept_job/(?P<slug>[-\w]+)/$', views.accept_jobs, name='accept_jobs'),
    url(r'^cancel_job/(?P<slug>[-\w]+)/$', views.cancel_job, name='cancel_job'),
    url(r'termandcondition/', views.termandcondition, name='termandcondition'),

    


]



##	url(r'^leassondeatil/(?P<slug>[-\w]+)/$', views.leassondeatil, name='leassondeatil'),
