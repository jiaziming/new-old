
from django.urls import path,re_path,include

from App01 import views




urlpatterns = [

        re_path(r'^$',views.index),
        re_path(r'^p1/$',views.page1),
        re_path(r'^p1_1/$',views.page1_1),
        re_path(r'^book/$',views.book),
        re_path(r'^book_from/',views.book_from),


]

