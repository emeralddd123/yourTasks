from datetime import datetime  
from datetime import timedelta

from django.db import models
from TaskManager.settings import AUTH_USER_MODEL as User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateTimeField(default=datetime.now() + timedelta(days=1)) 
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        ordering = ['expiry_date']
        get_latest_by = 'created_at'
        
        
        
