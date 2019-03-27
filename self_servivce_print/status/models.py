from django.db import models


# 用户表
class User(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=11)
    email = models.EmailField(max_length=32)
    UD = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'  # 数据库名
        verbose_name_plural = '用户表'


# 部门表
class Department(models.Model):
    department = models.CharField(max_length=12)

    def __str__(self):
        return self.department

    class Meta:
        db_table = 'Department'  # 数据库名
        verbose_name_plural = '部门表'
