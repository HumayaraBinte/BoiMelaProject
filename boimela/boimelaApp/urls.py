from django.urls import path, include
from . import views
from .views import dashboard, StallDetailView

urlpatterns = [
path('', views.home, name='boimelaApp-home'),
path('stall/<int:pk>/', StallDetailView.as_view(), name='stall-detail')
]
