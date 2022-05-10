from django.urls import path
from home import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


app_name = ""
urlpatterns = [
    path('home/', views.home, name="Home"),
    path('aboutus/', views.aboutus, name="Aboutus"),
    path('accounts/register/', views.register, name = "Register"),
    path('accounts/logout/', LogoutView.as_view(template_name='home/registration/logout.html'), name='Logout'),
    path('accounts/login/', views.login_request, name="login"),
    path('accounts/editar_perfil/', views.editarPerfil, name = 'Editar_perfil'),
    path('accounts/agregar_avatar/', views.agregarAvatar, name= "Agregar_avatar"),
    path('accounts/password_change/done/', views.password_change_done, name = 'password_done'),
    path('accounts/mi_perfil/', views.miPerfil, name="Mi_Perfil"),
    path('contacto/', views.contacto, name = "Formulario_Contacto"),
    path('contactook/', views.contacto_enviado, name = "Contacto_Enviado"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)