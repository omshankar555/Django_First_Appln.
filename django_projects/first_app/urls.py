from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'first_app/login_1.html'}, name = 'login'),
    url(r'^logout/$', logout, {'template_name': 'first_app/logout_1.html'}, name = 'logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name': 'first_app/reset_password.html', 'post_reset_redirect': 'password_reset_done', 'email_template_name': 'first_app/reset_password_email.html'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'first_app/reset_password_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'first_app/reset_password_complete.html'}, name='password_reset_complete'),
    url(r'^upload/$', views.image, name='image_blog')
]

"""
    url(r'^entry-expense/$', views.entry_expense, name='entry_expense'),
    url(r'^time/$', views.today_is, name='blog_time'),
    url(r'^upload/$', views.image, name='image_blog')

"""

