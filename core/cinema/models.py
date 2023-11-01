from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    date = models.CharField(max_length=10)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
