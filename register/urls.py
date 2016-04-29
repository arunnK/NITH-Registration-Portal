from django.conf.urls import patterns,include, url
from register.views import *
from django.views.generic import ListView
app_name='register'
urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^index.html$',index,name='index1'),
	url(r'^login.html$',login_view,name='my_login`'),
	url(r'^submissions.html$',submit,name='submit`'),
	url(r'^register.html$', register,name='register'),
	url(r'^registered/$',registered,name='registered'),
	url(r'^login/check/$',logincheck,name='logincheck'),
	url(r'^home/(?P<username>[^/]+)/step1$',home,name='home'),
	url(r'^home/(?P<username>[^/]+)/logout/$',my_logout,name='my_logout'),
	url(r'^home/(?P<username>[^/]+)/step1/getfee/$',getfee,name='getfee'),
	url(r'^home/(?P<username>[^/]+)/pay1/$',pay1,name='pay1'),
	url(r'^home/(?P<username>[^/]+)/pay1/pay1check/$',pay1check,name='pay1check'),
	url(r'^home/(?P<username>[^/]+)/step2$',step2,name='step2'),
	url(r'^home/(?P<username>[^/]+)/step2/getfee2/$',hostel_getfee,name='getfee2'),
	url(r'^home/(?P<username>[^/]+)/pay2/$',pay2,name='pay2'),
	url(r'^home/(?P<username>[^/]+)/pay2/pay2check/$',pay2check,name='pay2check'),
	url(r'^home/(?P<username>[^/]+)/step3$',step3,name='step3'),
	url(r'^home/(?P<username>[^/]+)/pay3/$',pay3,name='pay3'),
	url(r'^home/(?P<username>[^/]+)/pay3/pay3check/$',pay3check,name='pay3check'),
	url(r'^home/(?P<username>[^/]+)/thanks$',thanks,name='thanks'),
	url(r'^home/(?P<username>[^/]+)/thanks/pdf/$',print_users,name='pdfgen'),
]
