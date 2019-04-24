from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request,'blog/index.html')

def data(request,name='Django'):
    return HttpResponse(f"Welcome to data mr. {name}")

def page_year_view(reqeust,year):
    return HttpResponse(f"you are seeking pages for the year {year}")

def page_month_view(request,year,month):
    return HttpResponse(f"You are seeeking pages for the month {month} of year {year}")

def page_day_view(request,year,month,day):
    return HttpResponse(f"You are seeking specific to date {year}/{month}/{day}")