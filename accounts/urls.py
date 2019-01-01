

from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'),
	#path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	#path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
	#path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	#path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	#path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
	url(r'^register/', views.register, name='register'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.getuserprofile, name='getuserprofile'),
	url(r'^usertype/', views.usertype, name='usertype'),
	url(r'^useraddress/', views.useraddress, name='useraddress'),
	url(r'^useraddressedit/', views.useraddressedit, name='useraddressedit'),
	url(r'^userqualification/', views.userqualification, name='userqualification'),
	url(r'^userprofileedit/', views.userprofileedit, name='userprofileedit'),
	url(r'^userqualificationedit/(?P<slug>[-\w]+)/$', views.userqualificationedit, name='userqualificationedit'),






]