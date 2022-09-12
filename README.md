# api_yamdb
api_yamdb
## Название:
YaMDB
### Описание:
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории. 
На произведение можно добавить ревью с оценкой. К ревью можно оставить комментарий.
#### Технологии: 
Django==2.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0
django-filters==2.2.0
### Запуск проекта в dev-режиме:
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


### Активные сопровождающие проекта:
Артем Денисов
```
https://github.com/ardenisov
```

Владислав Бочкарев
```
https://github.com/PostHaineku
```

Мария Петрова
```
https://github.com/MyMilkie
```

### Загрузка database из csv:

После выполнения миграций загрузите тестовую database командой
```
python manage.py load_database
```

### Примеры запросов к api_yamdb:

Аутентификация:
```
http://127.0.0.1:8000/api/v1/auth/signup/
http://127.0.0.1:8000/api/v1/auth/token/
```

Получение списка и добавление жанров:
```
http://127.0.0.1:8000/api/v1/genres/
```

Удаление жанра:
```
http://127.0.0.1:8000/api/v1/genres/{slug}/
```

Добавление произведения:
```
http://127.0.0.1:8000/api/v1/titles/
```

Получение информации о произведении, частичное обновление информации, удаление:
```
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```

Добавление нового отзыва:
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```

Полуение отзыва по id, частичное обновление, удаление:
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```

Получение списка всех комментариев к отзыву, добавление комментария к отзыву:
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

Получение комментария к отзыву, частичное обновление комментария, удаление:
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Получение списка всех пользователей, добавление нового пользователя, :
```
http://127.0.0.1:8000/api/v1/users/
```

Получение пользователя по username, изменение данных пользователя, удаление:
```
http://127.0.0.1:8000/api/v1/users/{username}/
```

Получение данных своей учетной записи, изменение данных своей учетной записи:
```
http://127.0.0.1:8000/api/v1/users/me/
```
