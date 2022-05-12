from django.urls import path
from home import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


app_name = ""
urlpatterns = [
    path('home/', views.home, name="Home"),
    path('acerca_de_nosotros/', views.aboutus, name="Acerca_de_nosotros"),
    path('cuentas/register/', views.register, name = "Register"),
    path('accounts/logout/', LogoutView.as_view(template_name='home/registration/logout.html'), name='Logout'),
    path('cuentas/login/', views.login_request, name="login"),
    path('cuentas/editar_perfil/', views.editarPerfil, name = 'Editar_perfil'),
    path('cuentas/agregar_avatar/', views.agregarAvatar, name= "Agregar_avatar"),
    path('cuentas/password_change/done/', views.password_change_done, name = 'password_done'),
    path('cuentas/mi_perfil/', views.miPerfil, name="Mi_Perfil"),
    path('cuentas/', views.contacto, name = "Formulario_Contacto"),
    path('contactook/', views.contacto_enviado, name = "Contacto_Enviado"),
    path('cuentas/edit_profile/', views.editarBioyWeb, name="Edit_profile"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)