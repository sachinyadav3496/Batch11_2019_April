from django.contrib import admin
from django.urls import path,include 
#from mysite.views import index,data  
from mysite import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('blog/',include('blog.urls')),
    path('data/',views.data),

]
