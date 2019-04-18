
from django.http import HttpResponse 
from django.shortcuts import render 

def index(request):
    return render(request,'index.html',{'title':'HOME'})
    # page = """<h1 style='color:red'>
    # Welcome First Django Powered Web Page</h1>
    # <a href="/">Home</a>
    # <a href="/data/">Data</a>
    # """
    # return HttpResponse(page) 

def data(request):
    return render(request,"data.html",{'title':'DATA'})
   