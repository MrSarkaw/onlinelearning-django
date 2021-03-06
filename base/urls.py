from unicodedata import name
from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('room/<str:id>', views.room, name="room"),
    path("createroom",views.roomCreate, name='roomCreate'),
    path("updateRoom/<str:pk>",views.roomUpdate, name="updateRoom"),
    path("deleteRoom/<str:pk>",views.deleteRoom, name="deleteRoom"),
    path("deleteMessage/<str:pk>",views.deleteMessage, name="deleteMessage"),
    path("login", views.loginPage, name="loginPage"),
    path('register', views.registerPage, name="register"),
    path("logout", views.logoutPage, name="logoutPage"),
    path('profile/<str:id>', views.profile, name="profile"),
    path('profile/user/edit', views.profileEdit,name='profileEdit')
]