from django.urls import  path

from  core.cinema.views import GenreView
urlpatterns = [
    path('',GenreView.as_view())
]