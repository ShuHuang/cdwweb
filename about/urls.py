from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'),
    path('about/', views.about, name='about-about'),
    path('reader/', views.about, name='about-reader'),
    path('citing/', views.citing, name='about-citing'),
    path('contact/', views.contact, name='about-contact'),
    path('acknowledgement/', views.acknowledgement, name='about-acknowledgement'),
    re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),

]
