from B.views import *
from django.urls import path
app_name='B'
urlpatterns=[
    path('third_class/',third_class,name='third_class'),
    path('fourth_class/',fourth_class,name='fourth_class'),
]