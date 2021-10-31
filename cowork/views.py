from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login


def index(request):
  user = request.user
  return render(request, 'index.html', {'user':user})

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'


