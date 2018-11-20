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
        return '[grade] name:{0},date:{1},girlnum:{2},boynum:{3}'.format(self.name,self.date,self.girlnum,self.boynum)


class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default="True")
    age = models.IntegerField()
    content = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    #关联外键
    grade = models.ForeignKey('Grades',on_delete=models.CASCADE)

    def __str__(self):
        return '[student] name:{0},gender:{1},age:{2},content:{3},grade:{4}'.format(self.name,self.gender,self.age,self.content,self.grade)

