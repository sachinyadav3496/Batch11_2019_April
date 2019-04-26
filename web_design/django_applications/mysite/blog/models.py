from django.db import models
from django.contrib.auth.models import User 


class Blog(models.Model) : 
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    date_publish = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(default=None)
    def __str__(self):
        return self.title+'-'+self.author.username 



