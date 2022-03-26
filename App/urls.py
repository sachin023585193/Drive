from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('drive/',views.index,name='index'),
]