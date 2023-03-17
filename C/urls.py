from C.views import *
from django.urls import path
app_name='C'
urlpatterns=[
    path('fifth_class/',fifth_class,name='fifth_class'),
    path('sixth_class/',sixth_class,name='sixth_class'),
]