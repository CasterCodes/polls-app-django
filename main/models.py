from django.db import models

from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_test = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now()

    def __str__(self) -> str:
        return self.question_test

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice
