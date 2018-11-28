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
        db_table = "grades"


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    def createStudents(self, name, age, gender, content, grade, lastTime, createTime, isDele=False):
        stud = self.model()
        stud.name = name
        stud.age = age
        stud.gender = gender
        stud.grade = grade
        stud.content = content
        stud.lastTime = lastTime
        stud.createTime = createTime
        stud.isDelete = isDele
        return stud


class Students(models.Model):
    # 自定义模型管理器
    # 当自定义后，Students.object就会找就到，应使用Students.stuObj.get()....
    # stuObj = models.Manager()
    # 自定义的管理器用于筛选过滤
    stuObj2 = StudentsManager()

    name = models.CharField(max_length=20)
    gender = models.BooleanField(default="True")
    age = models.IntegerField(db_column='age')  # 设置表头名称
    content = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    grade = models.ForeignKey('Grades', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    # 设置元信息
    class Meta():
        # 数据库表名
        db_table = "students"
        # 对象默认的排序字段
        ordering = ['id']  # ['-id']降序

    @classmethod
    def createStudents(cls, name, age, gender, content, grade, lastTime, createTime, isDele=False):
        stu = cls(name=name, age=age, gender=gender, content=content, grade=grade, createTime=createTime,
                  lastTime=lastTime,
                  isDelete=isDele)
        return stu
