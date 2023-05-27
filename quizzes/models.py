from django.db import models
import uuid

QUIZ_CHOICES = (
    ("active" , "Active"),
    ("inactive" , "Inactive"),
    ("finished" , "Finished"),
)

class Quiz(models.Model):
    question = models.CharField(max_length=100)
    options =  models.JSONField()
    right_answer = models.IntegerField()
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(choices = QUIZ_CHOICES,max_length=10,default="inactive")
