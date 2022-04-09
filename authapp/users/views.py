from django.urls import reverse_lazy
from django.views.generic import CreateView
from . forms import CreationForm
from django.shortcuts import render


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html'


def home(request):
    template = 'home.html'
    key = 'Главная'
    context = {
        'key': key,
    }
    return render(request, template, context)