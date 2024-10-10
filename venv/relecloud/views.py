from django.shortcuts import render
from django.urls import reverse_lazy
from . import models 
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

# Vistas básicas
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def cruises(request):
    all_cruises = models.Cruise.objects.all()
    return render(request, 'cruises.html', {'cruises': all_cruises})

# Vista detalle para Destination
class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

# Vista detalle para Cruise
class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

# Crear InfoRequest con un formulario crispy
class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    form_class = models.InfoRequestForm 
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

# CRUD para Destination
class DestinationCreateView(generic.CreateView):
    model = models.Destination
    form_class = models.DestinationForm  # Formulario desde models.py
    template_name = 'destination_form.html'
    success_url = reverse_lazy('destinations')

class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    form_class = models.DestinationForm
    template_name = 'destination_form.html'
    success_url = reverse_lazy('destinations')

class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = 'destination_confirm_delete.html'
    success_url = reverse_lazy('destinations')

# CRUD para Cruise
class CruiseCreateView(generic.CreateView):
    model = models.Cruise
    form_class = models.CruiseForm  # Formulario desde models.py
    template_name = 'cruise_form.html'
    success_url = reverse_lazy('index')

class CruiseUpdateView(generic.UpdateView):
    model = models.Cruise
    form_class = models.CruiseForm
    template_name = 'cruise_form.html'
    success_url = reverse_lazy('index')

class CruiseDeleteView(generic.DeleteView):
    model = models.Cruise
    template_name = 'cruise_confirm_delete.html'
    success_url = reverse_lazy('index')
