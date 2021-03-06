### Описание
#### Для чего нужен проект:
```
Проект api_yatube позволяет получить доступ к ответам ресурса используя запросы через API со стороны клиентских приложений, 
будь то мобильные пользовательские решения или корпоративное ПО.
Все адреса проекта дотупны для чтения.
Для создания постов, комментариев необходимо создать учетную запись.
Получить TOKEN
по адресу - /auth/jwt/create/:
```
### Установка
#### Как запустить проект:
```
Клонировать репозиторий и перейти в него в командной строке:
git clone git@github.com:TimofeyVorobiev/api_final_yatube.git
cd api_final_yatube
```
```
Cоздать и активировать виртуальное окружение:
python -m venv env
source env/bin/activate
```
```
Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt
```
```
Выполнить миграции:
python manage.py makemigrations
python manage.py migrate
```
```
Запустить проект:
python manage.py runserver
```
### Примеры
#### Что можно запустить и проверить в проекте:
```
Проект доступен по адресу
Ознакомиться с полным функционалом и примерами можно по адресу http://127.0.0.1:8000/redoc
```
```
по адресу - /api/v1/posts/:
запросом GET - получить список всех постов
запросом POST - добавить свой пост
```
```
по адресу - api/v1/posts/{post_id}/comments/:
запросом GET - получить список комментариев определенного поста
запросом POST  - добавить комментарий к посту
```
