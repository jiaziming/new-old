from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('welcome to payment index')




def special_case_2003(request):

    print(special_case_2003)

    return HttpResponse('special_case_2003....')



def year_archive(request,year):
    print("--->",year)
    return HttpResponse(year)


def month_archive(request,year,month):
    print("--->", year,month)
    return HttpResponse("%s/%s" %(year,month))


def article_detail(request,year,month,article,file_type):
    print("--->", year,month,article,file_type)
    return HttpResponse("%s/%s-[%s.%s]" %(year,month,article,file_type))