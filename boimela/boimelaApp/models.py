from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Stall(models.Model):
    BOOK = 'BK'
    FOOD = 'FD'
    STALL_TYPES = (
        (BOOK, 'Book'),
        (FOOD, 'Food'),
    )
    stall_name= models.CharField(max_length=100)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    stall_type= models.CharField(max_length=2, choices=STALL_TYPES, default="Type N/A")

    class Meta:
        ordering= ('stall_name',)

    def __str__(self):
        return self.stall_name

class Book(models.Model):
    SCIFI = 'SF'
    ACTION = 'AC'
    HORROR = 'HR'
    ROMANTIC = 'RM'
    BOOK_GENRES = (
        (SCIFI, 'SCI-FI'),
        (ACTION, 'ACTION'),
        (HORROR, 'HORROR'),
        (ROMANTIC, 'ROMANTIC'),
    )
    book_name= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    isbn= models.IntegerField()
    book_genre= models.CharField(max_length=2, choices=BOOK_GENRES, default="Type N/A")
    release_date= models.DateField()
    stalls= models.ManyToManyField(Stall)

    class Meta:
        ordering= ('book_name',)

    def __str__(self):
        return self.book_name
