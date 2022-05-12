# ProyectoMascota

Realizado en conjunto Paula Ortiz Menne y Yamil Piñero. No hay algo especifico que haya realizado cada uno, sino que realmente lo hemos hecho juntos, ya que vivimos juntos por lo que nos poniamos a analizar, realizar, registrar, etc ambos.

La web funciona para cargar, buscar y ver listado completo de las mascotas cargadas. También para registrar, visualizar, editar y borrar Post en Blog.

las apps se llaman mascotasapp, blog y home. Todas las plantillas están en la carpeta template,
la plantilla base.html contiene un cuerpo base que contiene el titulo de la web y un pié de agradecimiento por la visita al sitio.

Cuenta con login, y una vez logueado se puede visualizar el perfil de ese usuario.

Para agregar mascota con nombre, edad, dueño y color ingresar a la ruta nuestras_mascotas/formulario/
Para buscar una mascota ya agregada ingresar a la ruta nuestras_mascotas/busqueda/
Para ver el listado completo de los datos cargados de todas las clases de models ingresar a nuestras_mascotas/lista/

Para ver las mascotas cargadas en Post la ruta es localhost
Para ver registrar un Post la ruta es formulario_blog/

Para enviar un mensaje de contacto la ruta es contacto/

Para visualizar el about us la ruta es acerca_de_nosotros/

Como base de datos utilizamos PostgreSQL 13
tambien instalamos psycopg2 para conectarnos, Pillow para que reconozca imagenes

No pudimos utilizar un editor de texto ya que no encontramos un instructivo en los pdf de las clases, y al tratar de instalar CKEditor nos arrojaba error y no lo pudimos hacer funcionar.

Pudimos crear el modelo Profile para agregar bio y website_url a User. Nos deja agregarlo desde un form, pero luego no nos permite editarlo desde un form.

Creamos modelo Avatar para darle una imagen a User, podemos agregarla mediante form, pero luego cuando la actualizamos con un form, Django sigue tomando la primera imagen y no la actualiza. Además no logramos que Avatar se visualizara en todas las views.

Intentamos resolver ambos inconvenientes siguiendo los pasos de los pdf de las clases, pero no lo hemos logrado, ya que los mismos presentan bastantes errores y hasta se encuentran incompletos.
