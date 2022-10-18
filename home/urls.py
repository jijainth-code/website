from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns =[path("",views.test , name='test'), 
                path("home/",views.home , name='home'),
                path("projects/",views.projects , name='projects'),
                path("contact/",views.contact , name='contact'),
                path("about/",views.about , name='about'),
                path("ai/" , views.ai , name ="ai")
                ]


urlpatterns += staticfiles_urlpatterns()