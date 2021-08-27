
from django.db import models

# Create your models here.
'''
1.定义模型类
2.模型迁移
    2.1生成迁移文件，数据库和模型的对应的关系
    python manage.py makemigrations
    2.2 生成表
    python manage.py migrate
3.操作数据库
'''
# 用户登录密码表
class LoginInfo(models.Model):
    # 主健会自动生成
    username=models.CharField(max_length=20)
    password=models.IntegerField()
    def __str__(self):
        return self.username
    # class Meta:
    #     # 修改表名
    #     # db_table="logininfo-1"
    #     verbose_name="用户登录信息"
# 用户信息表
class UserInfo(models.Model):
    gender_choices=((0,'male'),(1,'female'))

    username = models.CharField(max_length=20)
    age=models.IntegerField()
    # 枚举
    gender=models.SmallIntegerField(choices=gender_choices,default=0,verbose_name='女')
    aihao=models.ForeignKey(LoginInfo,on_delete=models.CASCADE)

