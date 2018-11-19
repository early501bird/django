from django.db import models


# Create your models here.

class Grades(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    girlnum = models.IntegerField()
    boynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)


class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default="True")
    age = models.IntegerField()
    content = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)

    #关联外键
    grade = models.ForeignKey('Grades')
