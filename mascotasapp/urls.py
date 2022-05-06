"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from . import views

urlpatterns = [
    path('nuestras_mascotas/', views.nuestras_mascotas, name = 'Nuestras_mascotas'),
    path('nuestras_mascotas/lista/', views.listado_animales, name = "Lista"),
    path('nuestras_mascotas/formulario/', views.formulario, name = "Formulario"),
    path('nuestras_mascotas/busqueda/', views.busqueda_mascota, name = "Busqueda"),
    path('nuestras_mascotas/buscar/', views.resultado_busqueda, name = "Resultado"),
]