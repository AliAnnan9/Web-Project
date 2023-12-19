from django.urls import path
from . import views
from .views import CarDetailView, HomeView , VecDetailsView ,BuyView
urlpatterns = [
    path('',HomeView.as_view(), name = "Home" ),
    path('Cars',CarDetailView.as_view(), name='Cars'),
    path('Cars/<int:pk>',VecDetailsView.as_view(), name = "Car-detail"),
    path('Cars/<int:pk>/Buy',BuyView.as_view(), name = "BuyCar"),
]
