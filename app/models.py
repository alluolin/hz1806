from django.db import models

# Create your models here.


# 定义数据模型类

# 定义一个学生类
# 注意: modle中定义的类需要继承 models.Model
class  Student(models.Model):
    s_name = models.CharField(max_length=50)
    s_age = models.IntegerField(default=18)













