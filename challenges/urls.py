from . import views
from django.urls import path


urlpatterns =[
    path("<int:month>",views.monthly_challange_by_number),
    path("<str:month>",views.monthly_challange,name="monthly_challanges"),

]