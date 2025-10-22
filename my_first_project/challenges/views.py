from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    "december": None
}

def home(request):
    month_list=list(monthly_challanges.keys())
    path=reverse("monthly_challanges", args=[month_list])
    return render(request, "challenges/index.html",{
        "month_list":month_list,
        "path":path,
    })

def monthly_challange_by_number(request, month):
    try:
        path=reverse("monthly_challanges",args=[list(monthly_challanges.keys())[month-1]])
        return HttpResponseRedirect(path)
    except:
        return HttpResponseNotFound("choose a number of the month")


def monthly_challange(request, month):
    try:
        monthly_challange_text=monthly_challanges[month]
        return render(request, "challenges/challange.html",{
            "text":monthly_challange_text,
            "month":month,

        })
    except:
        raise Http404()
    