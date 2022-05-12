from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('formulario_blog/', views.formulario_blog, name = 'Formulario_blog'),
    path('borrar_blog/<titulo_blog>/', views.borrar_blog, name = "Borrar_blog"),
    path('editar_blog/<titulo_blog>/', views.editar_blog, name = "Editar_blog"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)