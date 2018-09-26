from django.contrib import admin
from first_app.models import UserProfile

# Register your models here.

#admin.site.register(UserProfile)
#admin.site.site_title = 'Admin Page'
#admin.site.site_header = 'Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website' )

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queyset = queryset.order_by('user')
        return queyset

# To rename the column name (Description as Information) in admin page!
    user_info.short_description= 'Information'

admin.site.register(UserProfile, UserProfileAdmin)