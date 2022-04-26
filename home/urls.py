from django.urls import path
from home import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = ""
urlpatterns = [
    path('', views.home, name="Home"),
    path('aboutus/', views.aboutus, name="Aboutus"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name = "Register"),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='Logout'),
]