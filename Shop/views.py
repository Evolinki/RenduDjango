from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.
#def index(request):
 #   return render(request,'index.html')
 
def index(request):
    context ={}
    context["dataset"] = Product.objects.all()
         
    return render(request, "index.html", context)


def show(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
    

 
def create(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('index')
    return render(request, "create.html", {'form': form})
     

def update(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, "update.html", {'product': product})

def delete(request, id):
    form = Product.objects.get(id = id)
    form.delete()
    return HttpResponseRedirect('/')
    