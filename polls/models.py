# Models app deffing Question look. 
# Remember to Migrate by run 'python manage.py makemigrations' 
# if changes made to models.
# Run 'python manage.py migrate'
import datetime
from django.db import models
#added
from django.utils import timezone
from django.contrib import admin
#Added to make Question for the Admin Panel
class Question(models.Model):                         #Important Line
    question_text = models.CharField(max_length=200)  #Important Line
    pub_date = models.DateTimeField('date published') #Important Line
    #added for Adding Question Text
    def __str__(self):
        return self.question_text
    #time codes added.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # admin display modfication
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Publish recently?',   
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#Added to make Choice for Admin Panel
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #added for question text
    def __str__(self):
        return self.choice_text
# Create your models here.
