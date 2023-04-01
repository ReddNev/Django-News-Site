# Clone the repository:
```shell
    >>> https://github.com/ReddNev/Django-News-Site.git
```

# Go to the project folder:
```shell
    >>> cd my_site
```

# Installing the virtual environment:
```shell
    >>> python -m venv venv
```

# Launching the virtual environment:
```shell
    >>> venv/Scripts/activate
```

# How to start:
``` shell
    >>> python manage.py runserver
```

# How to make a migration:
```shell
  >>> python manage.py makemigrations
  >>> python manage.py migrate
```

# How to download dumb DB: 
```shell
  >>> python manage.py makemigrations
  >>> python manage.py migrate
  >>> python manage.py loaddata ./news/fixtures/data.json
```

# To manage records in the DB through the admin panel, create a superuser:  
```shell
    >>> python manage.py createsuperuser
```


# Login to admin panel:
```shell
    >>> http://127.0.0.1:8000/admin/
```
# Router: 
```shell
   >>> http://127.0.0.1:8000/api/news/
```
# Request examples:
```shell
    >>> GET /api/news/17/
```
# Response:
# {
    "id": 17,
    "title": "Корпоративный шлюз веб-безопасности: какие требования предусмотреть для замещения иностранной системы",
    "content": Текущий год внес существенные корректировки в планы многих торым стало главным вектором развития...
    "created_at": "2022-10-29T09:54:51.224663Z",
    "update_at": "2023-01-28T14:14:35.008909Z",
    "photo": "http://127.0.0.1:8000/media/photos/2022/11/02/ja600.jpg",
    "is_published": true,
    "views": 1,
    "category": 5
}
# Create router:
```shell
    >>> http://127.0.0.1:8000/api/news/create/
```
