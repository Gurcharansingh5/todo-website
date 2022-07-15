
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('authlogin',views.authlogin,name= 'authlogin'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    # path('updateuser',views.updateuser,name="updateuser")
]
