
from django.contrib import admin
from django.urls import path,include
from config.views import index  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('grras/',include('grras.urls')),
    path('blog/',include('blog.urls')),
]
