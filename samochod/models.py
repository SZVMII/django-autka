from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


class Part(models.Model):
    enumBodyType = [('sedan', 'Sedan'), ('kombi', 'Kombi'), ('hatchback', 'Hatchback'), ('cabriolet', 'Kabriolet'),
                    ('coupe', 'Coupe'), ]
    enumStatus = [('oczekujace', 'Oczekujące'), ('zaakceptowane', 'Zaakceptowane'), ('odrzucone', 'Odrzucone')]
    model = models.CharField(max_length=255, null=True)
    mark = models.CharField(max_length=255, null=True)
    startOfProduction = models.IntegerField(null=True)
    endOfProduction = models.IntegerField(null=True)
    engines = models.CharField(max_length=255, null=True)
    bodyType = models.CharField(max_length=255, choices=enumBodyType, default='sedan')
    partName = models.CharField(max_length=255)
    partOpis = models.CharField(max_length=1000)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=enumStatus, default='oczekujace')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    ratingEnum = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length=255, choices=ratingEnum, default='1')
