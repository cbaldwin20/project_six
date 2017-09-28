from django.conf.urls import url

from . import views 


urlpatterns = [
	#for the homepage
	url(r'^$', views.minerals_list, name='home'),
	#'http://localhost:8000/1/'   for the mineral details page
	url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
	
]