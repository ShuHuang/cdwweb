from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='about-home'),
    path('about/', views.about, name='about-about'),
    path('citing/', views.citing, name='about-citing'),
    path('contact/', views.contact, name='about-contact'),
    path('acknowledgement/', views.acknowledgement, name='about-acknowledgement'),
    re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),
    path('reader/', views.reader, name='about-reader'),
    path('finder/', views.finder, name='about-finder'),
    path('retriever/', views.retriever, name='about-retriever'),
    path('summariser/', views.summariser, name='about-summariser'),
    path('paraphraser/', views.paraphraser, name='about-paraphraser'),
    path('generator/', views.generator, name='about-generator'),
]
