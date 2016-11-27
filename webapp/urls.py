from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/home')),
	url(r'^home/$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_ok/$', TemplateView.as_view(
			template_name='registration/signup_ok.html'),
			name='signup_ok'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^search/$', views.search_movie, name="search"),
]