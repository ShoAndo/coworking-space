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
from .models import Seat, Store


def index(request):
  store = get_defalt_store()
  seats = store.seats.filter(user=None)
  contents = {
    'store': store,
    'seats': seats,
  }

  if request.user.is_authenticated: 
    user = request.user
    contents['user'] = user
    user_seat = Seat.objects.filter(user=user)
    if user_seat:
      res_seat = user_seat[0]
      contents['res_seat'] = res_seat

  return render(request, 'index.html', contents)

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'


class Logout(LoginRequiredMixin, LogoutView):
  template_name = 'index.html'

@login_required
def reserve(request, seat_id):
  seat = Seat.objects.get(id = seat_id)
  return render(request, 'reserve.html', {'seat':seat})

@login_required
def reserve_confirm(request):
  seat = Seat.objects.get(id = request.POST['seat_id'])
  seat.user = request.user
  seat.save()
  return render(request, 'confirm.html')

