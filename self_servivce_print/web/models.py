from django.db import models
from django.utils import timezone


# 项目表
class Project(models.Model):
    status_choice = (
        (1, '初期'),
        (2, '中期'),
        (3, '后期'),
        (4, '完成'),
    )
    pro_name = models.CharField(max_length=32)  # 项目名称
    team_leader = models.CharField(max_length=32)  # 负责人
    summary = models.CharField(max_length=64)  # 项目简介
    status = models.IntegerField(choices=status_choice)  # 状态

    def __str__(self):
        return self.pro_name

    class Meta:
        db_table = 'Project'  # 数据库名
        verbose_name_plural = '博客表'


#  项目内容表
class Content(models.Model):
    content = models.TextField()  # 内容
    comments = models.CharField(max_length=100)
    PC = models.OneToOneField(Project, on_delete=models.CASCADE)  # 和项目表一对一关联

    class Meta:
        db_table = 'Content'  # 数据库名
        verbose_name_plural = '内容表'


# 时间表
class Time(models.Model):
    """项目创建时间"""
    add_time = models.DateTimeField(auto_now_add=False)
    PT = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Time'  # 数据库名
        verbose_name_plural = '时间表'
