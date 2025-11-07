from django.urls import path
from webapp import views
urlpatterns=[path('home/',views.home,name='home'),
             path('about/',views.about,name='about'),
             path('contact/',views.contact,name='contact'),
             path('shop/',views.shop,name='shop'),
             path('filtered/<cat>/',views.filtered,name='filtered'),
             path('sign_in/',views.sign_in,name='sign_in'),
             path('sign_up/',views.sign_up,name='sign_up'),
             path('singlepage/<int:pid>',views.singlepage,name='singlepage')
             ]