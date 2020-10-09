from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('services/',views.services,name='services'),
    url('about-us/',views.about,name='about'),
    url('case-studies/',views.case_studies,name='case'),
    url('blog/',views.blog,name='blog'),
    url('leadership/',views.leadership,name='leadership'),
    url('digital-marketing',views.digital,name='digital'),
    url('our-approach/',views.approach,name='approach'),
    url('careers/',views.career,name='career'),
    url('our-team/',views.team,name='team'),
    url('recognition/',views.recognition,name='recog'),
    url('our-purpose/',views.purpose,name='purpose'),
    url('team-building',views.building,name='building'),
    url('change-management/',views.change,name='change'),
    url('conflict-resolution/',views.conflict,name='conflict'),
    url('talent-empowerment/',views.talent,name='talent'),
    url('contact-us/',views.contact,name='contact'),
    url('FAQ/',views.questions,name='FAQ')
]