from django.contrib import admin
from home.models import Post  #, Friend
from first_app.models import UserProfile

class PostProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info')

    def get_queryset(self, request):
        queryset = super(PostProfileAdmin, self).get_queryset(request)
        queyset = queryset.order_by('-created')
        return queyset

    def user_info(self, obj):
        return obj.created

# To rename the column name (Created as Posted On) in admin page!
    user_info.short_description= 'Posted On'

admin.site.register(Post, PostProfileAdmin)
