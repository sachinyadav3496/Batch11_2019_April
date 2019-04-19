

from django.urls import path 
from grras import views 

urlpatterns = [

    path('',views.index,name='grras')
]