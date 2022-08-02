from datetime import date
from datetime import timedelta
from django.utils.text import slugify
from django.urls import reverse
import string, random
from django.db import models
from TaskManager.settings import AUTH_USER_MODEL as User



def generate_random_slug():
    return ''.join(random.choice(string.digits) for _ in range(12))


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=True, null=True)
    task_due_date = models.DateField(blank=True,null=True,default=date.today() + timedelta(days=1)) 
    task_due_time = models.TimeField(blank=True,null=True)     
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task:tasks')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + generate_random_slug())
        super(Task, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Task'
        ordering = ['user']
        get_latest_by = 'created_at'
        

