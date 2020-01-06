from django.urls import path 
from . import views 

app_name = 'account'

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
]