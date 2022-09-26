# zebrands
Python 3.10
Django 3.2

Para poder ejecutar, se debe crear el ambiente se debe instalar las siguientes librerias.

Requirements.txt

asgiref==3.5.2
Django==3.2
django-ckeditor==6.5.1
django-ckeditor-5==0.2.0
django-js-asset==2.0.0
django-model-utils==4.0.0
djangorestframework==3.13.1
Pillow==9.2.0
psycopg2-binary==2.9.3
pytz==2022.1
sqlparse==0.4.2
Unipath==1.1

Al tener instalado el entorno se debe ejecutar:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage runserver

para ver las rutas solo se debe ejecutar en el navegador

127.0.0.1:8000

la ruta del aplicativo en donde se encuentran los CRUD es:

127.0.0.1:8000/index/

la ruta en donde se encuentra la pagina que veran los usuarios anonimos:

127.0.0.1:8000/page/



