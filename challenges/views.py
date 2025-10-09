from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challanges= {
    "january": "Work harder!",
    "february": "Keep the momentum!",
    "march": "Stay consistent!",
    "april": "Push through challenges!",
    "may": "Keep growing!",
    "june": "Halfway there, stay strong!",
    "july": "Don’t lose focus!",
    "august": "Keep improving!",
    "september": "Push your limits!",
    "october": "Stay disciplined!",
    "november": "Finish strong!",
    "december": "Reflect and prepare for next year!"
}

def index(request):
    return HttpResponse("This works!")

def monthly_challange_by_number(request, month):
    try:
        path=reverse("monthly_challanges",args=[list(monthly_challanges.keys())[month-1]])
        return HttpResponseRedirect(path)
    except:
        return HttpResponseNotFound("choose a number of the month")


def monthly_challange(request, month):
    try:
        return HttpResponse(monthly_challanges[month])
    except:
        return HttpResponseNotFound("choose the month")