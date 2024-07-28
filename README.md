# Необходимые шаги:

---

Для запуска проекта необходимо совершить следующее:

- Развернуть виртуальное окружение .venv
- Установить зависимости с помощью pip install -r requirements.txt
- Создать базу данных
- Создать и заполнить файл .env по шаблону .env.sample

- Применить миграции с помощью python manage.py migrate

Запустить следующие команды (каждую в своём процессе)
- redis-server
- celery -A config worker -l info
- celery -A config beat
- python manage.py runserver
