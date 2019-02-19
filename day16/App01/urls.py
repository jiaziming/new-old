
from django.urls import path,re_path,include
from App01 import views




urlpatterns = [

        re_path(r'^$',views.index)
]
