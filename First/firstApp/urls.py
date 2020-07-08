from django.urls import path
from . import views
urlpatterns = [
    path('',views.Main,name='Main'),
    path('Admin/',views.admin,name='Admin'),
    path('login/',views.login,name='Login'),
    path('index1/',views.index1,name='index1'),
    path('index2/',views.index2,name='index2'),
    path('ModifyTrain/',views.ModifyTrain,name='ModifyTrain'),
    path('AdminOpt/',views.AdminOpt,name='AdminOpt'),
    path('index3/',views.index3,name='index3'),
    path('index4/',views.index4,name='index4'),
    path('reg/',views.reg,name='reg'),
    path('index5/',views.index5,name='index5'),
    path('logout/',views.logout,name='logout'),
    path('showtickets/',views.showtickets,name='showtickets'),
    path('User/',views.User,name='User'),
    path('ModifyUser/',views.ModifyUser,name='ModifyUser'),
    path('train/',views.train,name='addtrain')
]