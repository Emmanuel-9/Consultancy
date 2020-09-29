from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('services/',views.services,name='services'),
    url('about-us/',views.about,name='about'),
    url('coaching/',views.coaching,name='coaching'),
    url('register',views.registration,name='register'),
    url('accounts/', include('django.contrib.auth.urls')), 
    url('profile/',views.profile,name='profile'),
    url('FAQ/',views.questions,name='FAQ'), 
    url('update-profile',views.update_profile,name='update'),
    url('cart/',views.cart,name='cart'),
    url('messages/',views.message,name='messages'),
    url('notifications',views.notifications,name='notifications')
]