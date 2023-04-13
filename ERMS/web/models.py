from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题',max_length=32)

class Userinfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='姓名')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    creat_time = models.DateTimeField(verbose_name='入职时间')
    depart = models.ForeignKey(to="Department",to_field='id',on_delete=models.CASCADE) # 级联删除 on_delete=models.CASCADE
    depart = models.ForeignKey(to="Department",to_field='id',null=True,blank=True,on_delete=models.SET_NULL) # 置空 null=True,blank=True,on_delete=models.SET_NULL
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)  # django约束只能1，2