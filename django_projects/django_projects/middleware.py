import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('logout').lstrip('/'):
            logout(request)

        elif request.user.is_authenticated() and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            return None
        #else:
        #    return redirect(settings.LOGIN_URL)


"""
Requirements to run this Django Project:

1). Python 3.5 Version.

2). Installing Virtual Environment. (Already installed the env, just we need to activate using this path env\scripts\activate.bat insideSocio-Task working directory.)

3). Install Django Software. (I installed 1.10 version).

To Run this project:-

--> Open the command prompt terminal. And try the following steps:-

   1). Enter into the Downloaded Soacil-Task Folder..

2). Activate the Virtual Environment. using this syntax:-  env\scripts\activate.bat

3). enter into the django_projects folder.

4). Run the Django Server using this command. (python manage.py runserver)

5). Open the Webbrowser type the url as http://127.0.0.1:8000

6). We have to register by clicking register button at the top right corner. If u don't want to register directly u can login by this credentials.. 

Username : admin And Password : django_projects

"""