# ProyectoMascota

Realizado en conjunto Paula Ortiz Menne y Yamil Piñero. No hay algo especifico que haya realizado cada uno, sino que realmente lo hemos hecho juntos, ya que vivimos juntos por lo que nos poniamos a analizar, realizar, registrar, etc ambos.

La web funciona para cargar, buscar y ver listado completo de las mascotas cargadas. También para registrar, visualizar, editar y borrar Post en Blog.

las apps se llaman mascotasapp, blog y home. Todas las plantillas están en la carpeta template,
la plantilla base.html contiene un cuerpo base que contiene el titulo de la web y un pié de agradecimiento por la visita al sitio.

Cuenta con login, y una vez logueado se puede visualizar el perfil de ese usuario.

Para agregar mascota con nombre, edad, dueño y color ingresar a la ruta formulario/
Para buscar una mascota ya agregada ingresar a la ruta busqueda/
Para ver el listado completo de los datos cargados de todas las clases de models ingresar a lista/

Para ver las mascotas cargadas en Post la ruta es localhost
Para ver registrar un Post la ruta es formulario_blog/

Para enviar un mensaje de contacto la ruta es contacto/

Para visualizar el about us la ruta es aboutus/

Como base de datos utilizamos PostgreSQL 13
tambien instalamos psycopg2 para conectarnos, Pillow para que reconozca imagenes

No pudimos utilizar un editor de texto ya que no encontramos un instructivo en los pdf de las clases, y al tratar de instalar CKEditor nos arrojaba error y no lo pudimos hacer funcionar.
