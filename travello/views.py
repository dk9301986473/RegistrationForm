from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination

# Create your views here.
# def index(request):
#     dest1=Destination()
#     dest1.name='Mumbai'
#     dest1.desc='The city never sleep'
#     dest1.img='destination_1.jpg'
#     dest1.price=700
#     dest1.offer=True

#     dest2=Destination()
#     dest2.name='Hydrabad'
#     dest2.desc='First Biryani then sherwani'
#     dest2.img='destination_2.jpg'
#     dest2.price=650
#     dest2.offer=False

#     dest3=Destination()
#     dest3.name='Bengaluru'
#     dest3.desc='The beautiful city'
#     dest3.img='destination_3.jpg'
#     dest3.price=900
#     dest3.offer=True

#     dests=[dest1,dest2,dest3]

#     return render(request, "index.html",{'dests':dests})



#---------------getting data from database----#
def index(request):
    dests=Destination.objects.all()
    

    return render(request, "index.html",{'dests':dests})