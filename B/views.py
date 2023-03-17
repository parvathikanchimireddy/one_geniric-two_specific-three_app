from django.shortcuts import render

# Create your views here.
def third_class(request):
    return render(request,'third_class.html')
def fourth_class(request):
    return render(request,'fourth_class.html')