Правильная установка моего проекта:

    git clone -b master https://github.com/TYGOLKA/Django

Для создания нового виртуального окружения:

    python -m venv venv
    venv\Scripts\activate

Это для скачивания  библиотек:

    pip install -r req.txt

Это если появилась ошибка, This behaviour is the source of the following dependency conflicts.: 

    pip install protobuf==3.20.3

Заходим в директорию проекта:

    cd university_site

Делаем миграции:

    python manage.py makemigrations

    python manage.py migrate

Создайте пользователя (admin):

    python manage.py createsuperuser

Запускаем сайт:

    python manage.py runserver

В консоле нажимаем на ссылку (http://127.0.0.1:8000/) и ваш проект будет запущен.
