from django.conf.urls import include,url
urlpatterns= [
	url(r'^signup/$','account.views.signup', name = 'signup'),
	url(r'^signup_done/$', 'account.views.signup', name = 'signup_done'),
	url(r'^home/$', 'account.views.home', name = 'home'),
	url(r'^logout/$', 'account.views.logout', name = 'logout'),
	url(r'^activate/(?P<uid>\d+)/(?P<token>[0-9A-Za-z_\-]+)/$', 'account.views.activate', name='activate'),
]
