from django.urls import path
from webapp import views
urlpatterns=[path('home/',views.home,name='home'),
             path('about/',views.about,name='about'),
             path('contact/',views.contact,name='contact'),
             path('shop/',views.shop,name='shop'),
             path('filtered/<cat>/',views.filtered,name='filtered')]