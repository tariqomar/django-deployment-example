
from django.urls import path
from p_app import views

app_name = 'p_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/',views.user_login, name='user_login'),
]