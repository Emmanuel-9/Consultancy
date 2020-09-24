from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('services/',views.services,name='services'),
    url('contact/',views.contact,name='contact'),
    url('coaching/',views.coaching,name='coaching'),
    url('fees/',views.about,name='about'),
    url('family/',views.family,name='family'),
    url('individual',views.individual,name='individual'),
    url('corporate',views.corporate,name='corporate'),
    url('register',views.register,name='register') 
]