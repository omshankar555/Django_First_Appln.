from django.shortcuts import redirect, render


def login_redirect(request):
    return redirect('/first_app/login')

