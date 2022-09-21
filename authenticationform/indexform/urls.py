from django.urls import path
from . import views 


urlpatterns = [
    
    path('',views.home,name='home'),
    path('signup/',views.register,name='register'),
    path('signin/',views.login,name='signin'),
    path('signout/',views.logout,name='signout'),
    path('postview/',views.post_view,name='postview'),
    path('like/',views.like_post,name='like'),
    path('myprofile/',views.my_profile,name='myprofile'),
    path('searchbar/',views.search_bar,name='searchbar'),

]
