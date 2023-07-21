from django.contrib import admin
#引入要注册的模型
from wxcloudrun.models import Work, Score
# Register your models here.注册
admin.site.register(Work)
admin.site.register(Score)
# admin.site.register(User)
