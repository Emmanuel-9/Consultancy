from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('services/',views.services,name='services'),
    url('contact/',views.contact,name='contact'),
    url('coaching/',views.coaching,name='coaching'),
    url('fees/',views.fees,name='fees'),
    url('register',views.registration,name='register'),
    url('accounts/', include('django.contrib.auth.urls')), 
    url('profile/',views.profile,name='profile'),
    url('FAQ/',views.questions,name='FAQ') 
]