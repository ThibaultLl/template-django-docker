from django.urls import path

from .views import authentication, login_view
app_name = 'authentication'
urlpatterns = [
    path('', authentication, name='authentication'),
    path('login_view/', login_view, name='login_view'),
    
]