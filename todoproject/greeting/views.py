from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
def greeting(request):
    return render(request,'index.html')
def greeting(request):
    count = 23
    return render(request,'index.html',{'count':count})
def greeting(request):
    count = '<b>23</b>'
    return render(request,'index.html',{'count':count})
def greeting(request):
    students = ['Ajay', 'Vineeth','Sudheesh']
    return render(request,'index.html',{'students':students})
def greeting(request):
    count = 23
    return render(request,'index.html',{'count':count})
def greeting(request):
    my_object = {
        'name': 'John',
        'age': 25,
        'city': 'New York'
    }
    
    return render(request, 'index.html', {'my_object': my_object})
def greeting(request):
    my_objects = [
        {'name': 'John', 'age': 25, 'city': 'New York'},
        {'name': 'Jane', 'age': 30, 'city': 'San Francisco'},
        {'name': 'Bob', 'age': 20, 'city': 'Chicago'}
    ]
    context = {'my_objects': my_objects}
    return render(request, 'index.html', context)