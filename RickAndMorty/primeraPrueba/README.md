CREAR PRIMER PROYECTO DJANGO




FUENTES
Manual base
https://tutorial.djangogirls.org/es/


FUENTES PENDIENTE DE CONSULTAR
Parte de esta sección está basada en tutoriales por Geek Girls Carrots (https://github.com/ggcarrots/django-carrots).
Parte de este capítulo está basada en el django-marcador tutorial bajo la licencia Creative Commons Attribution-ShareAlike 4.0 internacional. El tutorial de django-marcador tiene derechos de autor de Markus Zapke-Gündemann et al.



MANUAL CREADO PARA LINUX-UBUNTU

QUE ES DJANGO
Django es un framework escrito en Python de aplicaciones web.

Se basa en el desarrollo de componentes, para crear web más fácil y rápidamente.

COMO FUNCIONA
Cuando llega la petición al servcidor web, toma la dirección de la página web e intenta averiguar qué hacer con ella.
Estp se realiza por el urlresolver de Django(archivo url.py donde están las URL Uniform Resource Locator).
Si coincide la URL, Django le pasa la solicitud a la función asociada, que se llama view (vista).
En las vistas es donde se escribe la lógica, podremos:
	- Acceder a una base de datos.
	- Comprobar los permisos
	- Mostrar información.

La vista genera una respuesta y Django la envia al navegador del usuario.


NECESIDAD DE CREAR "ENTORNOS VIRTUALES"
El entorno virtual ayuda a mantener un entorno de desarrollo para nuestro proyecto.
Aunque no obligatorio, es recomendable hacerlo cuando trabajemos en un proyecto concreto.

Virtualenv aísla tu configuración de Python/Django para cada proyecto.
Creamos el directorio donde queramos tener el virtualenv y accedemos a el:

mkdir rickandmorty
cd rickandmorty

Si lo hemos echo nunca antes instalamos la herramienta
sudo apt install python3-venv


Definimos el nombre del entorno virtual en este caso "myenv". Puedes usar cualquier otro nombre, pero sólo utiliza minúsculas y no incluyas espacio.

python3 -m venv myvenv

Este código crea un directorio llamado myvenv (o cualquier nombre que hayas elegido) que contiene nuestro entorno virtual (básicamente un montón de archivos y carpetas). Donde trabajaremos

Ejecutamos el entorno virtual

source myvenv/bin/activate

Sabrás que tienes virtualenv iniciado cuando veas que la línea de comando en tu consola tiene el prefijo (myvenv).

Ahora podremos definir en el las dependencias necesarias para nuestro proyecto.



INSTALACIÓN DE DJANGO Y DE DEPENDENCIAS

Acttualizamos pip que nos servirá para instalar las dependencias.

python -m pip install --upgrade pip

Creamos un archivo requirements.txt dentro del directorio. Dentro del fichero debes escribir el siguiente texto:

Ahora, ejecuta para instalar Django. Se requiere acceso a internet

pip install -r requirements.txt




CREACIÓN DE LA ESTRUCTURA DE UN PROYECTO DE DJANGO

Vamos a crear el esquema que tienen todos los proyectos de Django.
Los nombres de algunos archivos y directorios son muy importantes para Django. No deberías renombrar los archivos que estamos a punto de crear. Moverlos a un lugar diferente tampoco es buena idea. Django necesita mantener una cierta estructura para poder encontrar cosas importantes.

Recuerda ejecutar todo en el virtualenv. Si no ves un prefijo (myvenv) en tu consola tienes que activar tu virtualenv.

Escribimos el siguiente comando. El punto . es crucial porque le dice al script que instale Django en el directorio actual (para el cual el punto . sirve de abreviatura).

django-admin startproject nombreproyecto .

django-admin.py es un script que creará los archivos y directorios para ti. Ahora deberías tener una estructura de directorios parecida a esta:

nombredirectorio
├───manage.py
├───mysite
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
└───requirements.txt

En tu estructura de directorios, también verás el directorio myvenv que creamos anteriormente.

Para que sirve cada archivo del DIRECTORIO DEL PROYECTO
	manage.py es un script que ayuda con la administración del sitio. Con él podremos iniciar un servidor web en nuestro ordenador sin necesidad de instalar nada más, entre otras cosas.
	settings.py contiene la configuración de tu sitio web.
	urls.py contiene una lista de los patrones utilizados por urlresolver.
	
El resto de archivos no los vamos a cambiar. Pero es importante no borrarlos.



MODIFICAR LA CONFIGURACIÓN DEL PROYECTO EN SETTINGS.PY

Vamos a hacer algunos cambios en mysite/settings.py. Para saber más puedes leer https://docs.djangoproject.com/en/2.2/ref/settings/#language-code
Abre el archivo usando un IDE, por ejemplo pyCharm.

Configurarlo con el horario correcto. Ve a lista de Wikipedia de las zonas horarias y copia tu zona horaria (TZ) (e.g. Europa/Berlín).

En settings.py, encuentra la línea que contiene TIME_ZONE y modifícala para elegir tu zona horaria. Por ejemplo:

TIME_ZONE = 'Europe/Berlin'

Puedes añadir lo siguiente para cambiar el idioma de los botones y notificaciones de Django

LANGUAGE_CODE = 'es-es'


También tenemos que añadir una ruta para archivos estáticos. (Veremos todo acerca de archivos estáticos y CSS más adelante.) Ve al final del archivo, y justo debajo de la entrada STATIC_URL, añade una nueva llamada STATIC_ROOT:

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'



MIGRACIONES EN DJANGO
Para crear una base de datos para nuestro blog, ejecutemos lo siguiente en la consola:
python manage.py migrate 
(necesitamos estar en el directorio de que contiene el archivo manage.py). 
Si eso va bien, deberías ver algo así:

(myvenv) ~/nombreproyecto $ python manage.py migrate
Operations to perform:
  Apply all migrations: auth, admin, contenttypes, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK



INICIALIZACIÓN DEL SERVIDOR

Debes estar en el directorio que contiene el archivo manage.py. En la consola, podemos iniciar el servidor web ejecutando :

python manage.py runserver

Ahora necesitas revisar que tu website se está ejecutando. Abre tu navegador (Firefox, Chrome, Safari, Internet Explorer, o cualquiera que uses) y escribe esta dirección:

http://127.0.0.1:8000/

Enhorabuena! ¡Has creado tu primer sitio web y lo has iniciado usando un servidor web!


IMPORTANTE

Mientras el servidor web esté corriendo y esperando solicitudes adicionales, la terminal aceptará nuevo texto pero no ejecutará nuevos comandos.
Para escribir comandos adicionales mientras el servidor web está corriendo, abra una nueva ventana de terminal y active su virtualenv.

source myvenv/bin/activate

Para parar el servidor web, ve a la ventana donde se esté ejecutando y pulsa CTRL+C, las teclas Control y C a la vez.



UTILIZACIÓN DE BASES DE DATOS

Hay una gran variedad de opciones de bases de datos para almacenar los datos de tu sitio. Utilizaremos la que viene por defecto, sqlite3.

Esta ya está configurado en esta parte de tu archivo nombreproyecto/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




TAREAS PENDIENTES
Autenticacín de usuarios(registrarse, iniciar sesión, cerrar sesión)
Panel de administración para el sitio web
Formularios
Archivos
