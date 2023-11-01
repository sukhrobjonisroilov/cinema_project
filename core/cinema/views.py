from  rest_framework import generics




from core.cinema.serialezrs import GenreSerializer
from core.cinema.models import Genre

class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer




