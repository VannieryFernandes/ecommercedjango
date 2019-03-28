from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from catalog.models import Category
from .forms import ContactForm

def index(request):
	return render(request, 'index.html')

def product(request):
	return render(request, 'product.html')

def product_list(request):
	return render(request, 'product_list.html')


def contact(request):
  success = False
  form = ContactForm(request.POST or None)
  if form.is_valid():
  	sucess = True
  context = {
   'form' : form,
   'success':success
  }

  return render(request,'contact.html',context)