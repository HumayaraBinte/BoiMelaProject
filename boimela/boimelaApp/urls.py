from django.urls import path, include
from . import views
from .views import StallListView, StallDetailView, StallCreateView, StallUpdateView, StallDeleteView

urlpatterns = [
path('', views.home, name='boimelaApp-home'),
path('latest/', views.latest, name='boimelaApp-latest'),
path('dashboard/', StallListView.as_view(), name='dashboard'),
path('stall/<int:pk>/', StallDetailView.as_view(), name='stall-detail'),
path('stall/new/', StallCreateView.as_view(), name='stall-create'),
path('stall/<int:pk>/update/', StallUpdateView.as_view(), name='stall-update'),
path('stall/<int:pk>/delete/', StallDeleteView.as_view(), name='stall-delete'),
path('navigation/',views.navigation, name='boimelaApp-navigation'),
path('search/',views.searchposts, name='boimelaApp-search')
]
