from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^login/$', login, {'template_name': 'first_app/login_1.html'}),
    url(r'^logout/$', logout, {'template_name': 'first_app/logout_1.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),

    url(r'^time/$', views.today_is, name='blog_time'),
    url(r'^upload/$', views.image, name='image_blog')
]

"""
    url(r'^add/$', views.add, name='add_num'),
    url(r'^getinput/$', views.getinput, name='add_input'),
    url(r'^postinput/$', views.postinput, name='add_post') 
"""

