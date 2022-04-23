"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from . import views

urlpatterns = [
    path('lista/', views.listado_animales, name="Lista"),
    path('formulario/', views.formulario, name="Formulario"),
    path('busqueda/', views.busqueda_mascota, name="Busqueda"),
    path('buscar/', views.buscar, name="Buscar"),
]