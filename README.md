# Real-estate-agency-with-django
Django project about service of real estate agency

Quickstart run app:

### 1. Установить Docker на ПК - 
Windows:
$ https://docs.docker.com/docker-for-windows/install/

или

Mac: 
$ https://docs.docker.com/docker-for-mac/install/ 

### 2. Перейти в директорию agency в скачанном проекте
$ cd ./agency

### 3. Запустить команду, чтобы создать админа
$ docker-compose run web python manage.py createsuperuser

После чего в том же терминале дождаться строки 

$ Username (leave blank to use 'root'):

И ввести информацию о новом суперпользователе для админки

### 4. Запустить команду docker-compose up

$ docker-compose up

### Вроде бы всё ( ͡° ͜ʖ ͡°) 
