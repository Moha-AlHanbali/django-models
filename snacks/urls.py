from django.urls import path
from .views import HomeView, SnackListView, SnackDetailView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('snack_list', SnackListView.as_view(), name = 'snack_list'),
    path('snack_list/<int:pk>/', SnackDetailView.as_view(), name = 'snack_detail'),
]
