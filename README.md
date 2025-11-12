# Tree Menu Django App

Данный проект реализует древовидное меню на Django с хранением в базе данных и редактированием через стандартную админку.

**Автор:** Никандров Владислав ([Doshaniu](https://github.com/Doshaniu))

---

## Возможности

- Древовидное меню через template tag `{% draw_menu 'menu_name' %}`
- Активный пункт определяется по URL текущей страницы
- Ветви меню над активным элементом автоматически разворачиваются
- Поддержка нескольких меню на одной странице (по названию)
- Редактирование пунктов меню через стандартную админку Django
- Каждый вызов меню выполняет ровно 1 запрос к базе

---

## Быстрый старт

1. Клонируем репозиторий:

```
git clone https://github.com/Doshaniu/Tree-menu-test.git
cd Tree-menu-test
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt - установка зависимостей

выполняем миграции 
python manage.py makemigrations
python manage.py migrate

создаем суперпользователя для доступа к админке
python manage.py createsuperuser

заполняем бд из фикстуры
python manage.py loaddata menu_items.json

запускаем сервер
python manage.py runserver

```
