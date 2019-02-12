from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.



def db_handle(request):
    #数据库 增
    #models.userinfo.objects.create(username='alex',password='123456',age=123)
    #字典形式
    #dic = {'username':'eric','password':'123123','age':123}
    #models.userinfo.objects.create(**dic)


    #删除
    #models.userinfo.objects.filter(username='alex').delete()

    #修改
    #models.userinfo.objects.all().update(age=1)

    #查找
    # models.userinfo.objects.all()
    # models.userinfo.objects.filter(age=1)
    # models.userinfo.objects.filter(age=1).first()

    user_list_obj = models.userinfo.objects.all()
    #queryset list


    # for line in user_list_obj:
    #     print(line.username,line.age)


    #return HttpResponse('ok')
    return render(request,'t1.html',{'li':user_list_obj})





def home (request):
    return HttpResponse('app01.home')


def news(request,nid1,nid2):
    nid = nid1 + nid2
    return HttpResponse(nid)

