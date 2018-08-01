from django.urls import path
app_name="Auth"
from . import views
urlpatterns=[
path('login_page',views.login_page,name='Login'),
path('signup_page',views.signup_page,name='Signup'),
path('logout_page',views.logout_page,name='Logout')
]