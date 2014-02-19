from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = patterns('',
	url(r'^sounds/$', views.SoundList.as_view()),
	url(r'^sounds/(?P<pk>[0-9]+)/$', views.SoundDetail.as_view()),
	url(r'^annotations/$', views.AnnotationList.as_view()),
	url(r'^annotations/(?P<pk>[0-9]+)/$', views.AnnotationDetail.as_view()),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
	url(r'^api-auth/', include('rest_framework.urls',
								namespace='rest_framework')),
)
