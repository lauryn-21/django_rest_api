from django.db import models 
# from tasks.models import Task

# Create your models here.
class Task(models.Model):
    #title
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) #description
    completed = models.BooleanField(default=False)
    #completed
    created_at = models.DateTimeField(auto_now_add=True) #created_at

    def __str__(self):
        #return the task title
        return self.title
    
    # t = Task(title="Coding in Python",description="Building a REST API using django")
    # t.save()
    # Task.objects.all()