from django.urls import path
from . import views
from .views import FilmDetailView

urlpatterns = [
    path('',views.home, name = "Home" ),
    path('Cars/<int:pk>/Film',FilmDetailView.as_view(), name="ToFilm"),
    path('Cars/<int:pk>/FilmCreation',views.create_Appointment, name="ToFilmCrate"),
]