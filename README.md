##### Agregar archivos estáticos:  #####

```sudo docker-compose -f prod.yml run spacerental_prod python manage.py collectstatic --no-input ```

##### Ingresar al bash  #####

```sudo docker-compose -f prod.yml exec spacerental_prod bash ```

##### Running project #####

First of all you have to install all package to the container to do this you need to run:

```docker-compose -f dev.yml build```

After that commanad running successfully you need to create a env folder and then inside it create dev.env ask the folks by te enviromenta variables to set up inside it, after dev.env did set up run the next command:

```docker-compose -f dev.yml up```

##### Create tenant #####

To create tenant first you have to enter to the shell python from:

``` python manage.py shell ```

after that, you have to run the upcoming commands:

```tenant = Client(domain_url='localhost', schema_name='public', name='public')```
```tenant.save()```


##### Create superuser tenant #####

To create an user to tenant you have to run the upcoming command:

```python manage.py createsuperuser --username=admin --schema=public```

Note:

if you have to create an user to specific tenant give the name tenant to --schema.

https://docs.python.org/3/library/ftplib.html