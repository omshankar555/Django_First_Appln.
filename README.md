

Pre- Requirements:

1). Python 3.5 Version.

2). Install an Virtual Environment. 

3). Install Django Software using, pip install "django==1.10" (I installed Django 1.10 version).


    To Run this project:-

--> Open the command prompt terminal. And try the following steps:-

    ..> Enter into the Downloaded Django_First_Appln Folder..

    ..> Activate the Virtual Environment. using this syntax:-  env\scripts\activate.bat

    ..> Enter into the django_projects folder in terminal command prompt.

    ..> Run the Django Server using this command --> python manage.py runserver

    ..> Open the Webbrowser type the url as http://127.0.0.1:8000

    ..> Then you may have to create super user to access the webapp, follow this command 
                --> python manage.py createsuperuser

    ..> Then you may have to migrate the database, follow these command,
                >> python manage.py check 
                >> python manage.py makemigrations 
                >> python manage.py migrate
