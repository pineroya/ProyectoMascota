from django.urls import path
from home import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = ""
urlpatterns = [
    path('', views.home, name="Home"),
    path('aboutus/', views.aboutus, name="Aboutus"),
    path('accounts/register/', views.register, name = "Register"),
    path('accounts/logout/', LogoutView.as_view(template_name='home/registration/logout.html'), name='Logout'),
    path('accounts/login/', views.login_request, name="login"),
    path('editarperfil/', views.editarPerfil, name = 'Editar_perfil'),
    path('accounts/password_change/done/', views.password_change_done, name = 'password_done'),
]
# ^accounts/password_change/$ [name='password_change']x
# ^accounts/password_change/done/$ [name='password_change_done']
# ^accounts/password_reset/$ [name='password_reset']
# ^accounts/password_reset/done/$ [name='password_reset_done']
# ^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^accounts/reset/done/$ [name='password_reset_complete']
