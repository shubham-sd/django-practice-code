from django.shortcuts import render
from .models import Details
from django.http import HttpResponse
# from django.template import loader

# Create your views here.
# def home(request):
#     template = loader.get_template('html/index.html')
#     return HttpResponse(template.render())

# def home(request):
#     return render(request, 'html/index.html')

def insert_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']

        mod = Details(name=name, age=age)
        mod.save()

        return HttpResponse("Data Saved 😺")
    else:
        # return HttpResponse("Data Not Saved 😿")
        return render(request, 'html/index.html')


def show_data(request):
    data = Details.objects.all()

    show_data = {
        "detail": data
    }

    return render(request, 'html/index.html', show_data)