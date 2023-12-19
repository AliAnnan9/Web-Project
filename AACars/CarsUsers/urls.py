from django.urls import path
from . import views
from .views import AboutUsView ,RegisterView , MassegeView

urlpatterns = [
    path('', views.home, name="Home"),
    path('AboutUs', AboutUsView.as_view(), name="AboutUs"),
    path('UserRegisteration',RegisterView.as_view(),name="Register"),
    path('SuccessMassege', MassegeView.as_view(),name="Massege"),
]
