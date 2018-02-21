from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from geofood.models import Restaurant

def home(request):
    geomap=Restaurant.objects.get(id=1)
    return render(request, "home.html", {'geomap':geomap})

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'