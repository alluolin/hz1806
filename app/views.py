import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#视图函数---用来处理数据逻辑

# request 是请求参数
from app.models import Student


def hello(request):

    return  HttpResponse("hz1805班的helloword")


def template(request):
    #相应一个html文件,
    # ctrl + p  参看方法的参数
    # 参数1: request.请求提
    # 参数2: template_name 模板名
    return render(request,"templateTest.html")


# 保存一个学生
def saveStudent(request):
#     创建一个学生
    student = Student()
    student.s_name = "习胖胖" + str(random.randint(1,100))
    student.s_age = random.randint(1,100)

#    保存到数据库
    student.save()

    return  HttpResponse("插入成功了")



# 展示数据
def queryStudent(request):
#     查询数据
#  获得所有student
    students = Student.objects.all()
    print(students)
    return  render(request,"students.html",context={"students":students})












