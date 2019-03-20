from django.shortcuts import render,HttpResponse

# Create your views here.
from  App01 import models

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



def book(request):

    if request.method == "POST":
        print(request.POST)
        book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        print('--->',request.POST.get('author_ids'))
        author_ids = request.POST.getlist('atuhor_ids')


        print(book_name,publisher_id,author_ids)


        new_book = models.book(
            name = book_name,
            publisher_id = publisher_id,
            publisher_date = '2016-05-22'
        )

        new_book.save()
        new_book.authors.add(*author_ids)



    book = models.book.objects.all()
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()


    return render(request.App01/book.html,{'books':book,
                                           'pulishers':publisher_list,
                                           'authors':author_list
                                           })



def book_from(request):

  return render(request,'App01/book_from.html')




def year_archive(request,year):
    print("--->",year)
    return HttpResponse(year)


def month_archive(request,year,month):
    print("--->", year,month)
    return HttpResponse("%s/%s" %(year,month))


def article_detail(request,year,month,article,file_type):
    print("--->", year,month,article,file_type)
    return HttpResponse("%s/%s-[%s.%s]" %(year,month,article,file_type))




