from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Stall, Book
# Create your views here.
def home(request):
    return render(request, 'boimelaApp/index.html')

@login_required
def dashboard(request):
        context= {
        'stalls': Stall.objects.all()
        }
        return render(request, 'boimelaApp/dash.html', context)

class StallDetailView(DetailView):
    model= Stall
