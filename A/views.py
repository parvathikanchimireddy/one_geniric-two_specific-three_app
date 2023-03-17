from django.shortcuts import render

# Create your views here.
def first_class(request):
    return render(request,'first_class.html')
def second_class(request):
    return render(request,'second_class.html')