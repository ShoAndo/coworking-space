from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import get_defalt_store
from .models import Seat


def index(request):
  user = request.user
  store = get_defalt_store()
  seats = store.seats.all()
  contents = {
    'user': user,
    'store': store,
    'seats': seats
  }
  return render(request, 'index.html', contents)

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'



class Logout(LoginRequiredMixin, LogoutView):
  template_name = 'index.html'

def reserve(request, seat_id):
  seat = Seat.objects.get(id = seat_id)
  return render(request, 'reserve.html', {'seat':seat})

@login_required
def reserve_confirm(request):

  seat = Seat.objects.get(id = request.POST['seat_id'])
  seat.user = request.user
  seat.save()
  return render(request, 'confirm.html')
