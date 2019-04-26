from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog 
# Create your views here.
def index(request):
    all_blog = Blog.objects.all().order_by('-date_publish')
    data = []
    for each_blog in all_blog : 
        blog = { 
            'title': each_blog.title, 
            'topics' : each_blog.topic,
            'author' : each_blog.author.username,
            'content' : each_blog.content,
            'date_publish' : each_blog.date_publish, 
        }
        data.append(blog)

    return render(request,'blog/index.html',{'data':data})

def data(request,name='Django'):
    return HttpResponse(f"Welcome to data mr. {name}")

def page_year_view(reqeust,year):
    return HttpResponse(f"you are seeking pages for the year {year}")

def page_month_view(request,year,month):
    return HttpResponse(f"You are seeeking pages for the month {month} of year {year}")

def page_day_view(request,year,month,day):
    return HttpResponse(f"You are seeking specific to date {year}/{month}/{day}")