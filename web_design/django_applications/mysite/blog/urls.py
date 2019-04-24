from django.urls import path 
from blog import views 
urlpatterns = [ 
    path('',views.index,name='blog'),
    path('data/',views.data),
    path('data/<str:name>/',views.data),
    path('pages/<int:year>/',views.page_year_view),
    path('pages/<int:year>/<int:month>/',views.page_month_view),
    path('pages/<int:year>/<int:month>/<int:day>/',views.page_day_view),
]

