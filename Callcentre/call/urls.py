from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
   path('',views.home,name='home'),
   path('Login',views.Login,name='Login'),
   path('layoutstatic',views.layoutstatic,name='layoutstatic'),
   path('layoutsidenavlight',views.layoutsidenavlight,name='layoutsidenavlight'),
   path('register',views.register,name='register'),
   path('password',views.password,name='password'),
   path('Error401',views.Error401,name='Error401'),
   path('Error404',views.Error404,name='Error404'),
   path('Error500',views.Error500,name='Error500'),
   path('charts',views.charts,name='charts'),
   path('tables',views.tables,name='tables'),
   path('Disclaimer',views.Disclaimer,name='Disclaimer'),
]

