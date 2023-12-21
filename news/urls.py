from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('about/', aboutUs, name='about'),

    path('kino/', kino, name='kino'),
    path('music/', music, name='music'),
    path('actor/', actor, name='actor'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/',logout_user,name='logout'),
    path('profile/',profile,name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('post/<slug:post_slug>/', show_post, name='post'),
    path('postkino/<slug:post_slug>/', show_post_kino, name='postkino'),
    path('postmusic/<slug:post_slug>/', show_post_music, name='postmusic'),
    path('postactor/<slug:post_slug>/', show_post_actor, name='postactor'),

    path('addpage/', addpage, name='addpage'),

]
