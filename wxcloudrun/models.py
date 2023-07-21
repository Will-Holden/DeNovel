from datetime import datetime
from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名


# class User(AbstractUser):
#     id = models.AutoField
#     # username = models.CharField(max_length=50)
#     # password = models.CharField(max_length=50)
#     openid = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)

#     REQUIRED_FIELDS = ['password']
#     class Meta:
#         db_table = 'user'  # 数据处理表名
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name

class Work(models.Model):
    id = models.AutoField
    worktitle = models.CharField(max_length=50)
    gold = models.IntegerField(max_length=11, default=0)


    class Meta:
        db_table = 'work'
        verbose_name = '工作'
        verbose_name_plural = verbose_name
        
class Score(models.Model):
    id = models.AutoField
    score = models.IntegerField(max_length=11, default=0)
    openid = models.CharField(max_length=50)
    worktitle = models.CharField(max_length=50)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, default='')
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    class Meta:
        db_table = 'score'  # 数据处理表名
        verbose_name = '分数'
        verbose_name_plural = verbose_name

