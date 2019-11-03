# Requisitos #

Para poder ejecutar este proyecto, tanto en producción como en desarrollo, es necesario tener instalados lo siguiente:
- Docker  (https://docs.docker.com/docker-for-windows/install/)
- Docker componse (https://docs.docker.com/compose/install/)

En los enlaces que he puesto se encuentra la documentación del modo de instalación en los diferentes SO

# Ejecucion del proyecto #

Si es la primera vez que arrancas el proyecto debes ejecutar el siguiente comando para descargar y construir los conetenedores e imágenes necesarios para el proyecto

``` docker-compose -f dev.yml build  ```

Si ya has construido el proyecto debes ejecutar el siguiente comando para ejecutarlo:

``` docker-compose -f dev.yml up --build ```

La bandera ```--build``` solo es necesario si se ha realizado algún cambio en la configuración de Docker, incluyendo las variables de entorno

Si vas a ejecutar el proyecto en producción debes cambiar ````dev.yml```` por ```prod.yml``` y quitar la bandera ```-f```



## Ingresar al bash  ##

```sudo docker-compose -f dev.yml exec spacerental_prod bash ```

# Tecnologías #
A continuación listo las principales librerías que he utilizado con enlaces a sus documentaciones oficiales

- Python 3.7
- Framework Flask 1.1.1 (https://flask.palletsprojects.com/en/1.1.x/)
- Marshmallow (https://flask-marshmallow.readthedocs.io/en/latest/)
- FTPlib (https://docs.python.org/3/library/ftplib.html)
- Flask MongoAlchemy 0.7.2 (https://pythonhosted.org/Flask-MongoAlchemy/)
- Flask-RestFul  0.3.7 (https://flask-restful.readthedocs.io/en/latest/)

# NOTAS #
En ```.gitignore``` he comentado las lineas que a continuación listo para que se suban al repositrio y no tengaís problemas al arrancar el proyecto pero por seguridad es mejor no subir las variables de entorno al respositorio, cuando lo considiréis adecuando descomentarlo.

- .env
- .venv
- env/
- venv/
- ENV/
- env.bak/
- venv.bak/