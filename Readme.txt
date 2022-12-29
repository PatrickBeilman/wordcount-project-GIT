a counting website project

run this code in command promt/command line/terminal

Navigate to the wordcount-project-GIT folder to properly run commands
ex: \Users\jon\Desktop\wordcount-project-GIT

Creating a new project:
django-admin startproject "projectname"

Add an app to a project:
python manage.py startapp "appname"

Starting the server:
python manage.py runserver

Creating migrations:
python manage.py makemigrations

Migrate the database:
python manage.py migrate

Creating a super user for the admin panel:
python manage.py createsuperuser

Collecting static files into one folder:
python manage.py collectstatic
