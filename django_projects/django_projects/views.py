from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/first_app/login')