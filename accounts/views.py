from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.views.generic import CreateView,TemplateView, UpdateView, FormView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import PasswordChangeForm

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('login')

register = RegisterView.as_view()

class IndexView(LoginRequiredMixin,TemplateView):

    
    template_name = 'accounts/index.html'
    

index = IndexView.as_view()

class UpdateUserView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email', 'username', 'dt_nascimento']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

update_user  = UpdateUserView.as_view()

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm
    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
      form.save()
      return super(UpdatePasswordView, self).form_valid(form)

update_password = UpdatePasswordView.as_view()
    
