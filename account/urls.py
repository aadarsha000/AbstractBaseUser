from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('register/',views.user_registration, name="registration"),
    path('login',views.user_login, name="login"),
    path('home/', views.home, name="home")   
]
