from . import views as v
from django.urls import path
from django.contrib.auth.urls import views


app_name = 'users'

urlpatterns = [
    path('signup/', v.SignUp.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]