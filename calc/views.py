from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello world")

# def home(request):
#     return HttpResponse("<h1>Hello world</h1>")


# def home(request):
#     return render(request,'home.html')


#----passing data to page dynamically
def home(request):
    return render(request,'home.html',{'name':'Kailash'})


def add(request):
    # val1=request.GET['num1']
    # val2=request.GET['num2']

    # val1=int(request.GET['num1'])
    # val2=int(request.GET['num2'])

    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])

    

    res=val1+val2

    return render(request,'result.html',{'result':res})