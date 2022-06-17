from django.db import models
RATING = [
    (1,'*'),
    (2,'**'),
    (3,'***'),
    (4,'****'),
    (5,'*****'),

]
class Director(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(choices=RATING,default=5,null=True)
    text = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

