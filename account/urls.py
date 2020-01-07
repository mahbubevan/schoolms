from django.urls import path 
from . import views 

app_name = 'account'

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/manage_teacher',views.view_teacher,name='view_teacher'),
    path('dashboard/create_teacher',views.create_teacher,name='create_teacher'),
    path('dashboard/logout',views.logout_custom_user,name='logout_custom_user'),
]