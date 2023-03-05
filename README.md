# Comandos para iniciar con Django

## 1. Primer paso:
- Para crear un nuevo proyecto se utiliza el comando "pip install virtualenv"
- virtualenv -- version para revisar la version
- virtualenv venv para crear la carpeta con el proyecto
- Dentro de esa carpeta escrivir el comando source bin/activate
- Una vez activado el entorno virtual ya se puede utilizar el entorno virtual
- Seleccionar el interprete de python de venv

## 2. Segundo paso: Instalar Django
- pip install django para instalar django en este proyecto
- django-admin --version para ver su version
- python3 -m django --version es otra version para ver su version
- Para crear un proyecto es django-admin startproject **myproyectoname**
- Se crean varios archivos python que viene siendo el proyecto
- Para mejorar el ordenamiento de los archivos es: django-admin startproject **myproyectoname .**
- Ejecutando el server: python3 manage.py runserver 8000
 - Para crear una aplicacion se utiliza el comando python3 manage.py startapp <nameapp>

 ## 3. Base de datos
 - python manage.py migrate sirve para ejecutar todas las migraciones (BD)
 - Para crear las nuevas migraciones se usa el comando python3 manage.py makemigrations
 - Se crean los modelos con clases en el archivo models