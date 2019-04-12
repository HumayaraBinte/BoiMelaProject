from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Stall, Book
# Create your views here.
def home(request):
    return render(request, 'boimelaApp/index.html')

class StallListView(LoginRequiredMixin, ListView):
    model = Stall
    template_name= 'boimelaApp/dash.html'
    context_object_name= 'stalls'

    def get_queryset(self):
        return Stall.objects.filter(owner=self.request.user)


class StallDetailView(LoginRequiredMixin, DetailView):
    model= Stall
