from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('formularioblog/', views.formularioblog, name = 'Formulario_blog'),
    path('deleteblog/<titulo_blog>/', views.deletepost, name = "Delete_blog"),
    path('editarblog/<titulo_blog>/', views.editarblog, name = "Editar_blog"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)