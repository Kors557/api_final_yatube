# api_final
### Для чего этот проект:
Проект предназначен для предоставления доступа через API к социальной сети Yatube

### Стэк технологий:
Python, Dgango, Dgango Rest Framework, JWT

0. Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone git@github.com:Kors557/api_final_yatube.git
  ```

  ```
  cd api_final_yatube
  ```

1. Cоздать и активировать виртуальное окружение:

  ```
  python -m venv venv
  ```

  ```
  source venv/scripts/activate
  ```

2. Установить зависимости из файла requirements.txt:

  ```
  pip install -r requirements.txt
  ```

3. Выполнить миграции:

  ```
  python yatube_api/manage.py makemigrations
  ```

  ```
  python yatube_api/manage.py migrate
  ```

4. Запустить проект:

  ```
  python yatube_api/manage.py runserver
<<<<<<< HEAD
  ```
=======
  ```
>>>>>>> 7b32d1126dfe9b6409aeb939b63b88c28b64d415
