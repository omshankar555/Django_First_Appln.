

Requirements:

1). Python 3.5 Version.

2). Installing Virtual Environment. (Already installed the env, just we need to activate using this path env\scripts\activate.bat inside Django_First_Appln working directory.)

3). Install Django Software using pip install "django==1.10" (I installed 1.10 version).

To Run this project:-

--> Open the command prompt terminal. And try the following steps:-
1). Enter into the Downloaded Django_First_Appln Folder..

2). Activate the Virtual Environment. using this syntax:-  env\scripts\activate.bat

3). Enter into the django_projects folder in terminal command prompt.

4). Run the Django Server using this command --> python manage.py runserver

5). Open the Webbrowser type the url as http://127.0.0.1:8000

6). Then you may have to create super user to access the webapp, follow this command --> python manage.py createsuperuser

7). Then you may have to migrate the database, follow these command --> 
                python manage.py check 
                python manage.py makemigrations 
                python manage.py migrate
