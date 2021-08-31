from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True, default='a') # dafailt必要 argument of type 'NoneType' is not iterable というエラーが出て既読にできない

    def __str__(self):
       return self.title 
