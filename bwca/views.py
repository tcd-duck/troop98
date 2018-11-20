from django.shortcuts import render
from bwca.models import Camper
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import crispy_forms


def index(request):
    num_interested = Camper.objects.filter(commitment__iexact='Interested').count()
    num_committed = Camper.objects.filter(commitment__iexact='Committed').count()

    num_interested += num_committed

    context = {
        'num_interested': num_interested,
        'num_committed': num_committed,
        }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class CamperListView(generic.ListView):
    model = Camper


class CamperDetailView(generic.DetailView):
    model = Camper
    fields = ['first_name', 'last_name', 'email', 'role', 'commitment', 'week1',\
              'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8',\
              'notes'
              ]


def CamperStatusView(request):
    camper_context = Camper.objects.all()

    context = {
        'camper_context': camper_context,    }

    return render(request, 'status.html', context = context)



class CamperCreate(CreateView):
    model = Camper
    fields = ['first_name', 'last_name', 'email', 'role', 'commitment', 'week1',\
              'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8',\
              'notes'
              ]


class CamperUpdate(UpdateView):
    model = Camper
    fields = ['first_name', 'last_name', 'email', 'role', 'commitment', 'week1',\
              'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8',\
              'notes'
              ]


class CamperDelete(DeleteView):
    model = Camper
    success_url = reverse_lazy('campers')



def CamperAvailability(request):
    camper_context = Camper.objects.all()

    context = {
        'camper_context': camper_context,
        }

    return render(request, 'campers_available.html', context=context)

#
#
# class AvailableDateView(CreateView):
#     model = AvailableDate
#     fields = "__all__"
