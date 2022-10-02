
Fuentes
HOLA MUNDO
https://proyectoa.com/instalar-django-y-primera-aplicacion-web-hola-mundo-en-python/

QUE ES DJANGO

Django es un framework de Python

INSTALAR DJANGO CON PIP DE PYTHON
Antes de instalar Django, debemos comprobar que efectivamente no está instalado en nuestro sistema:

python -m django --version

Se requiere internet.Para instalar Django ejecutaremos el siguiente comando:

pip install Django

Ahora, ejecutando el siguiente comando, que nos devolverá la versión de Django instalada:

python -m django –version

Si necesitamos instalar una versión concreta de Django podemos usar el comando:

pip install Django==4.1


DIFERENCIA PROYECTO-APLICACION
Un proyecto puede contener múltiples aplicaciones; por ejemplo, en un proyecto web de facturación, una aplicación de este proyecto podría ser la gestión de albaranes, otra la gestión de proveedores y otra la gestión de facturas. Todas las aplicaciones formarían parte del proyecto de facturación.


CREAR PRIMER PROYECTO
Desde el terminal accederemos a la carpeta donde queramos que se guarde el proyecto
Ejecutaremos el siguiente comando para crear el proyecto en la carpeta en la que nos encontremos:

django-admin startproject hola_mundo

El comando creará una carpeta dentro de la carpeta en la que estemos con el nombre del proyecto. Creará también los ficheros básicos del proyecto en la raíz, manage.py.
Y __init__.py, asgi.py, settings.py, urls.py y wsgi.py en la subcarpeta del proyecto.



EJECUTAR DJANGO A TRAVÉS DE SU SERVIDOR
Probamos que funciona correctamente el servidor web que incorpora Django y que ejecuta nuestro proyecto. Deberemos estar en la subcarpeta que contiene el archivo manage.py
Se ejecuta con el siguiente comando:

python3 manage.py runserver

Django se ejecutará en el servidor http://127.0.0.1:8000/

Para apagar el servidor (Cuando esta ejecutandose el servidor no se ejecuta ningún comando del terminal) se usará Control + C
Si no esta ejecutandose el servidor no funciona Django.


MIGRACIONES
Para evitar el error que aparece al ejecutar el servidor web Django:

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run ‘python manage.py migrate’ to apply them.

Abrimos otro terminal. Ejecutaremos el comando:

python3 manage.py migrate


CREAR LA PRIMERA APLICACIÓN DEL PROYECTO

Para ello, desde la carpeta donde estay manage.py, ejecutaremos el comando:

python3 manage.py startapp home

Home es el nombre que usaremos para esta aplicación

Nos habrá creado otra subcarpeta con el nombre de la aplicación «home» con los ficheros básicos de la aplicación (admin.py, apps.py, models.py, tests.py, views.py):

ARCHIVOS BÁSICOS DE LA APLICACIÓN

    __init__.py: archivo especial de Python que indica que el contenido de esta subcarpeta será un módulo.
    admin.py: archivo de Django para registrar modelos y poder emplearlos en una aplicación para la gestión de datos.
    apps.py: archivo de configuración de la aplicación.
    migrations: carpeta para gestión de las migraciones.
    models.py: archivo para crear los modelos de la aplicación.
    tests.py: archivo para realizar pruebas de la aplicación.
    views.py: archivo para crear las funciones y vistas para la lógica de la aplicación. Será la capa de la lógica de negocio que se encarga de conectar la capa del modelo con la de la plantilla.
    
   
   
MOSTRAR UN "HOLA MUNDO"
Para mostrar «Hola mundo» en nuestra aplicación «home», editaremos el fichero «views.py».
En este caso editaremos los archivos con el ide PyCharm Comunity.

Agregaremos el siguiente código a este fichero:

from django.http import HttpResponse
 
def index(request):
    return HttpResponse('Hola Mundo. <br><br>Esto es una prueba de aplicación web con Django por <a href="https://proyectoa.com">Proyecto A</a>')
    
    
Ahora necesitaremos hacer el «ruteo» en la aplicación y el proyecto para que la aplicación sea accesible desde el servidor web Django. 
Para ello crearemos el fichero urls.py en la carpeta de la aplicación (en nuestro caso en la carpeta home) y lo editaremos, agregando el siguiente código:

from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
]


Y ahora editaremos el fichero urls.py que ya existe, ubicado en la carpeta del proyecto «rickAndmorty». Vemos que tiene la ruta para el acceso de la aplicación admin (que explicamos en el siguiente punto del artículo). 
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


MOSTRAR DATOS DESDE UNA API CON DJANGO
