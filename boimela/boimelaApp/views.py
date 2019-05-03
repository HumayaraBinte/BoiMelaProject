from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Stall, Book
# Create your views here.
def home(request):
    return render(request, 'boimelaApp/index.html')

def latest(request):
    book= Book.objects.all()
    return render(request, 'boimelaApp/latestbook.html', {'books':book})

def navigation(request):
    return render(request,'boimelaApp/navigation.html')

class StallListView(LoginRequiredMixin, ListView):
    model = Stall
    template_name= 'boimelaApp/dash.html'
    context_object_name= 'stalls'

    def get_queryset(self):
        return Stall.objects.filter(owner=self.request.user)

class StallDetailView(LoginRequiredMixin, DetailView):
    model= Stall

class StallCreateView(LoginRequiredMixin, CreateView):
    model= Stall
    fields= ['stall_name', 'stall_type']

    def form_valid(self, form):
        form.instance.owner= self.request.user
        return super().form_valid(form)

class StallUpdateView(LoginRequiredMixin, UpdateView):
    model= Stall
    fields= ['stall_name', 'stall_type']

    def form_valid(self, form):
        form.instance.owner= self.request.user
        return super().form_valid(form)

class StallDeleteView(LoginRequiredMixin, DeleteView):
    model= Stall
    success_url= '/dashboard'

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = book.objects.filter(Q(book_name__icontains=srch))

            if match:
                return render(request,'boimelaApp/search.html',{'sr':match})
            else:
                message.error(request,'no result found')
    return render(request,'boimelaApp/search.html')