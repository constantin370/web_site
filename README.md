# Blogicum
## О проекте
Проект "web_site" - это Сайт Визитка.
## Установка
- Клонируйте проект из гитхаба:\
`git clone git@github.com:constantin370/web_site.git`
- Создайте и активируйте виртуальное окружение:\
`python -m venv venv`\
`source venv/Scripts/activate`
- Установите зависимости из файла pyproject.toml:\
- poetry install
`pip install -r pyproject.toml`
- Перейдите в каталог с файлом manage.py, примените миграции:\
`cd/web_site/main_project`\
`python manage.py migrate`
- Запустите сервер:\
`python manage.py runserver`
## Авторы
* Константин Мурадян
