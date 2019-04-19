from django.shortcuts import render

def index(request):
    return render(request,'grras/index.html',{'title':"GRRAS"})

