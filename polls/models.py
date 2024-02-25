from django.db import models

# Create your models here.
class Hire(models.Model):
  mail =  models.CharField(max_length=50)  
  desc = models.TextField()
  def __str__(self):
        return self.mail

