from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    if request.method == 'GET':

        # user_info = {'user':'alex',
        #              'name':'Alex Li'}

        user_info = [

            {'username':'alex','name':'AlexLi1','age':19},
            {'username':'jack','name':'jackmat','age':12},
            {'username':'erio','name':'eroeorn','age':54},
            {'username':'pony','name':'ponytom','age':54},
        ]


        #print("user request:",request.GET.get('user'))
        return render(request,'App01/index.html',{'user_objs':user_info})




def page1(request):

    return render(request,'App01/page1.html')

def page1_1(request):

    return render(request,'App01/page_1.html')



def payment_url(reuest):

    return HttpResponse('Hello tuhao')


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