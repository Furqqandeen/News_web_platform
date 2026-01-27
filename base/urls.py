from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<cname>/',views.post_by_category,name='post_by_category'),
    path('article/<slug>/',views.single_article,name='single_article'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')
]

