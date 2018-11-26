from django.db import models


# Create your models here.
# 不需要定义主键，在生成时会自动添加，并且值为自动增加

class Grades(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    girlnum = models.IntegerField()
    boynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    class Meta():
        db_table="grades"


class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default="True")
    age = models.IntegerField()
    content = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    #关联外键
    grade = models.ForeignKey('Grades',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    #设置元信息
    class Meta():
        #数据库表名
        db_table="students"
        #对象默认的排序字段
        # ordering=['id'] #['-id']降序
