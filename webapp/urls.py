from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_ok/$', TemplateView.as_view(
			template_name='registration/signup_ok.html'),
			name='signup_ok'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': ''}, name="logout")
]