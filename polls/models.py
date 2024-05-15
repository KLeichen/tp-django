from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.question_text
    

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    date = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text
    
    def is_popular(self):
        return self.likes >= 3