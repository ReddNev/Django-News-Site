# Как запустить:
``` shell
    >>> python manage.py runserver
```
# Как сделать миграцию:
```shell
  >>> python manage.py makemigrations
  >>> python manage.py migrate
```
# Как загразить dumb DB: 
```shell
  >>> python manage.py makemigrations
  >>> python manage.py migrate
  >>> python manage.py loaddata ./news/fixtures/data.json
```
