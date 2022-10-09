ACCESO A LA APLICACIÓN ADMIN (ADMINISTRADOR)

FUENTES
Manual base
https://tutorial.djangogirls.org/es/

HOLA MUNDO
https://proyectoa.com/instalar-django-y-primera-aplicacion-web-hola-mundo-en-python/


FUENTES PENDIENTE DE CONSULTAR
Parte de esta sección está basada en tutoriales por Geek Girls Carrots (https://github.com/ggcarrots/django-carrots).
Parte de este capítulo está basada en el django-marcador tutorial bajo la licencia Creative Commons Attribution-ShareAlike 4.0 internacional. El tutorial de django-marcador tiene derechos de autor de Markus Zapke-Gündemann et al.

CONSUMIR APIS
https://www.dataquest.io/blog/python-api-tutorial/
https://gerasolis.wordpress.com/2021/02/20/como-consumir-una-api-de-clima-con-django/
https://pythonizando.com/consumir-una-api-rest-con-python-3-usando-requests/


MANUAL CREADO PARA LINUX-UBUNTU.
En este caso editaremos los archivos con el IDE PyCharm Comunity.

QUE ES DJANGO
Django es un framework escrito en Python de aplicaciones web.

Se basa en el desarrollo de componentes, para crear web más fácil y rápidamente.

En django es importante diferenciar entre un proyecto y una aplicación. Dentro de un mismo proyecto se crearán las diferntes aplicaciones: home, admin, characters... que corresponderá si así lo deseamos a diferentes url o páginas web de nuestro proyecto.


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

Cuando trabajes en un entorno virtual, python automáticamente se referirá a la versión correcta, de modo que puedes utilizar python en vez de python3.




INSTALACIÓN DE DJANGO Y DE DEPENDENCIAS

Acttualizamos pip que nos servirá para instalar las dependencias.

python -m pip install --upgrade pip

Creamos un archivo requirements.txt dentro del directorio. Dentro del fichero debes escribir el siguiente texto:

Ahora, ejecuta para instalar Django. Se requiere acceso a internet

pip install -r requirements.txt


DIFERENCIA PROYECTO-APLICACION
Un proyecto puede contener múltiples aplicaciones; por ejemplo, en un proyecto web de facturación, una aplicación de este proyecto podría ser la gestión de albaranes, otra la gestión de proveedores y otra la gestión de facturas. Todas las aplicaciones formarían parte del proyecto de facturación.



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

Para evitar el error que aparece al ejecutar el servidor web Django:

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run ‘python manage.py migrate’ to apply them.


Ejecutemos lo siguiente en la consola:

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


Si no esta ejecutandose el servidor no funciona Django.





CREACIÓN DE LA PRIMERA APLICACIÓN "HOME"

Home es el nombre que usaremos para esta aplicación. Para ello, desde la carpeta donde estay manage.py, ejecutaremos el comando:

python3 manage.py startapp home

Nos habrá creado otra subcarpeta con el nombre de la aplicación «home» con los ficheros básicos de la aplicación (admin.py, apps.py, models.py, tests.py, views.py):


ARCHIVOS BÁSICOS DE UNA APLICACIÓN

    __init__.py: archivo especial de Python que indica que el contenido de esta subcarpeta será un módulo.
    admin.py: archivo de Django para regiStrar modelos y poder emplearlos en una aplicación para la gestión de datos.
    apps.py: archivo de configuración de la aplicación.
    migrations: carpeta para gestión de las migraciones.
    models.py: archivo para crear los modelos de la aplicación.
    tests.py: archivo para realizar pruebas de la aplicación.
    views.py: archivo para crear las funciones y vistas para la lógica de la aplicación. Será la capa de la lógica de negocio que se encarga de conectar la capa del modelo con la de la plantilla.



MOSTRAR UN "HOLA MUNDO"

Necesitaremos hacer el «ruteo» en la aplicación y el proyecto para que la aplicación sea accesible desde el servidor web Django. 

Para ello crearemos el fichero urls.py (new > python file) en la carpeta de la aplicación (en nuestro caso en la carpeta home) y lo editaremos, agregando el siguiente código:

from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
]


Para mostrar «Hola mundo» en nuestra aplicación «home», editaremos el fichero «views.py».
Agregaremos el siguiente código a este fichero:

from django.http import HttpResponse
 
def index(request):
    return HttpResponse('Hola Mundo. <br><br>Esto es una prueba de aplicación web con Django.')
    
    


Y ahora editaremos el fichero urls.py que ya existe, ubicado en la carpeta del proyecto «rickandmorty». Vemos que tiene la ruta para el acceso de la aplicación admin (que explicamos en el siguiente punto del artículo). 
Añadiremos el import para la aplicación holaMundo y su ruta correspondiente, quedando:

from django.contrib import admin
from django.urls import path, include
from home import urls

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/', include('home.urls')),
]

Ya podremos iniciar el servidor web Django con el comando:

python3 manage.py runserver

Y desde un navegador web accederemos a la URL:

http://127.0.0.1:8000/home/

Mostrando nuestra primera aplicación web Django.

En el terminal podremos comprobar que cada vez que se accede al servidor web se añade una nueva línea de log:

[08/Jan/2022 22:25:33] «GET /home/ HTTP/1.1» 200 119



ACCESO A LA APLICACIÓN ADMIN (ADMINISTRADOR)

Django incorpora una app de administración (admin) a la que se puede acceder.  Para establecer un usuario y contraseña de acceso a la APLICACIÓN admin vamos al terminal y ejecutaremos el siguiente comando:

python manage.py createsuperuser

Nombre de usuario (leave blank to use 'monica'): monica
Dirección de correo electrónico: monica@gmail.com
Password: 
Password (again): 



Desde el navegador web, accederemos a la URL:

http://127.0.0.1:8000/admin

Nos solicitará usuario y contraseña. Introducimos lo que pusimos anteriormente y tendremos acceso a Django administration.

Esta web de administración no tiene muchas opciones, sirve como un ejemplo más de lo que se puede hacer con Django. Básicamente podremos crear y modificar usuarios y grupos y establecer permisos para estos usuarios:




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
