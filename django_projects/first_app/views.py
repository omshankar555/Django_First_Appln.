from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
import datetime

# Create your views here.
def index(request):
    numbers = [10,20,30,40,50]
    name = 'Bigdatamatica'

    args = {'myname' : name, 'numbers': numbers}
    return render(request, 'first_app/home.html', args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/first_app')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'first_app/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'first_app/profile.html', args)

#@login_required
def edit_profile(request):
    if request.method == 'POST':

        #form = UserChangeForm(request.POST, instance = request.user)
        ''' To edit all fields of the user '''
        form = EditProfileForm(request.POST, instance=request.user)
        """ To edit selected fields of the User """

        if form.is_valid():
            form.save()
            return redirect('/first_app/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'first_app/edit_profile.html', args)

#@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/first_app/profile')
        else:
            return redirect('/first_app/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'first_app/change_password.html', args)

def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body bgcolor = lightcyan><div><h2> Current date and time: {0}-{1}-{2} </h2> </div></body></html>".format(now.year, now.month, now.day)
    return HttpResponse(html)

def image(request):
    return render(request, 'first_app/image.html')

