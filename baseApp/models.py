from django.db import models
# built in django user model 
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
  # a user can have multiple tasks so add with a foreign key if a user is delete all the task will be deleted so using cascade allowing it to be null and in the form it can be black.
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  # the title should be a character field 
  title = models.CharField(max_length=200)
  # description is a text field and the user can keep it blank
  description = models.TextField(null=True, blank=True)
  # complete can be a boolen field mentioning yes or no by default will be false
  complete = models.BooleanField(default=False)
  # for created it will be a datetimefield and it will be automatically be true
  created = models.DateTimeField(auto_now_add=True)

  # want to pass string 

  def __str__(self):
    return self.title
  
  # for default ordering 

  class meta:
    ordering = ['complete']