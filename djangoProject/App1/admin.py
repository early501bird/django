from django.contrib import admin

# Register your models here.

from .models import Grades, Students


class StudentsInfo(admin.TabularInline):#StackedInline
    model = Students
    extra = 2

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]

    # 列表页属性
    # 展示表头
    list_display = ['pk', 'name', 'date', 'girlnum', 'boynum', 'isDelete']
    # 过滤器
    list_filter = ['name']
    # 搜索
    search_fields = ['name']
    # 分页
    list_per_page = 5
    # 添加/修改属性的顺序
    fields = ['name','boynum','girlnum','isDelete']
    # 给属性分组，注意field与fieldsets不能同时使用
    # fieldsets = [
    #     ('num', {'fields': ['girlnum', 'boynum''']}),
    #     ('base', {'fields': ['name', 'date', 'isDelete']}),
    # ]

#admin.site.register(Grades, GradesAdmin)


#由装饰器执行注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.gender : return '男'
        else: return '女'
    gender.short_description = '性别'
    list_display = ['pk', 'name', 'age', gender, 'content', 'grade', 'isDelete']
    list_per_page = 10

    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Students, StudentsAdmin)
# 正常可以由装饰器执行注册