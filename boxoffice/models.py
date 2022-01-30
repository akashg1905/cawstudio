from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.name, self.city.name)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance.id)
    return 'movie_{0}_{1}'.format(instance.name, filename)


class Movie(models.Model):
    name = models.CharField(max_length=20, unique=True)
    rating = models.FloatField(default=2.0)
    movie_genre = models.CharField(max_length=50, default="Action | Comedy | Romance")
    movie_duration = models.IntegerField(default=150)
    is_active = models.BooleanField(default=True)
    url = models.ImageField(upload_to=user_directory_path, default="")

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=20, unique=True)
    start_time = models.DateTimeField(default=datetime.now, blank=False)
    end_time = models.DateTimeField(default=datetime.now, blank=False)
    total_seats = models.IntegerField(default=40)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,default="")
    theatre=models.ForeignKey(Theatre, on_delete=models.CASCADE,default="")
    available_seats = models.IntegerField(default=40)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shows = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_no = models.IntegerField()

    @property
    def seat_no_as_list(self):
        return self.seat_no.split(',')
