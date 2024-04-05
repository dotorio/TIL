from django.shortcuts import render

# Create your views here.
def problem1(request):
    return render(request, 'weathers/problem1.html')

def problem2(request):
    return render(request, 'weathers/problem2.html')

def problem3(request):
    return render(request, 'weathers/problem3.html')

def problem4(request):
    return render(request, 'weathers/problem4.html')