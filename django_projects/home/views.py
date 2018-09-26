'''
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('It works')
'''

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm #, ReplyForm
from home.models import Post #, Friend

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        #friend = Friend.objects.get(current_user=request.user)
        #friends = friend.users.all()

        args = {
            'form': form, 'posts': posts, 'users': users
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


"""
post.objects.all()[1].post
post.get_next_by_created()
post.get_next_by_created().post
post.get_next_by_created().post
post.get_previous_by_created().post


    def get_reply(self, request):
        form = ReplyForm()
        postss = Post.objects.all().order_by('-created')
        userss = User.objects.exclude(id=request.user.id)
        #friend = Friend.objects.get(current_user=request.user)
        #friends = friend.users.all()

        args = {
            'form': form, 'posts': postss, 'users': userss
        }
        return render(request, self.template_name, args)

    def post_reply(self, request):
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.save()

            text = form.cleaned_data['reply']
            form = ReplyForm()
            return redirect('home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home')
"""