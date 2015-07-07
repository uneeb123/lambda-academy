from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^register/(?P<module_id>[0-9]+)/$', views.registration, name='registration'),
	url(r'^(?P<module_id>[0-9]+)/$', views.detail, name='module_detail'),
	url(r'^about/$', views.about, name='about'),
	url(r'^success/$', views.success, name='success'),
]