"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from .views import *
from . import views

urlpatterns = [
    #path('lista/', listado_perros),
    path('', views.listado_animales, name="ListaP"),
]