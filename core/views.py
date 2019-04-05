from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from catalog.models import Category
from .forms import ContactForm
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
index = IndexView.as_view()

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

