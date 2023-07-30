from django.contrib import admin
#引入要注册的模型
from wxcloudrun.models import Work, Score, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.注册
admin.site.register(Work)
admin.site.register(Score)
# admin.site.register(User)

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)