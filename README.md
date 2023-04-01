# Clone the repository:
```shell
    >>> https://github.com/ReddNev/Django-News-Site.git
```

# Переходим в папку с проектом:
```shell
    >>> cd my_site
```

# Устанавливаем виртуальное окружение:
```shell
    >>> python -m venv venv
```

# Запускаем виртуальное окружение:
```shell
    >>> venv/Scripts/activate
```

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

# Чтобы управлять записями в БД через админ панель, создайте суперпользователя:  
```shell
    >>> python manage.py createsuperuser
```


# Вход в админ панель:
```shell
    >>> http://127.0.0.1:8000/admin/
```
# Router: 
```shell
   >>> http://127.0.0.1:8000/api/news/
```
# Примеры запросов:
```shell
    >>> GET /api/news/17/
```
# Ответ:
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
