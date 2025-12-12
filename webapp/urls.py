from django.urls import path
from webapp import views
urlpatterns=[path('home/',views.home,name='home'),
             path('about/',views.about,name='about'),
             path('contact/',views.contact,name='contact'),
             path('shop/',views.shop,name='shop'),
             path('filtered/<cat>/',views.filtered,name='filtered'),
             path('sign_in/',views.sign_in,name='sign_in'),
             path('sign_up/',views.sign_up,name='sign_up'),
             path('singlepage/<int:pid>',views.singlepage,name='singlepage'),
             path('save_signup/',views.save_signup,name='save_signup'),
             path('user_login/',views.user_login,name='user_login'),
             path('user_logout/', views.user_logout, name='user_logout'),
path('save_message/', views.save_message, name='save_message'),
             path('cart/',views.cart,name='cart'),
             path('checkout/',views.checkout,name='checkout'),
             path('save_cart/',views.save_cart,name='save_cart')

             ]