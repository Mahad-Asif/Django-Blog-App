from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
     title = models.CharField(max_length=100) #The restricted textual data with maximum characters of 100.
     content = models.TextField() #TextField means the unrestricted textual data
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user gets deleted then you want to delete the that user-related posts as well.


     def __str__(self):
         return self.title

     def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk': self.pk})
