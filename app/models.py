from django.db import models

# Create your models here.

TODO_CHOICE = [
        ('weekly', 'weekly'),
        ('daily', 'daily')
]

class Todo(models.Model):
    
    # , 'weekly': weekly
    text = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=120, null=False, blank=False, choices = TODO_CHOICE, default="daily")
    
    def __str__(self):
        return self.type
    

    