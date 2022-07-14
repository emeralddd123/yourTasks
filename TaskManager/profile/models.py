from django.db import models
#from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _
from TaskManager.settings import AUTH_USER_MODEL as User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    username = models.CharField(
        _("username"),
        blank=True,
        null=True,
        unique=True,
        max_length=50
    )
    
    first_name = models.CharField(
        _("first name"),
        blank=True,
        null=True,
        unique=True,
        max_length=50
    )
    
    last_name = models.CharField(
        _("last name"),
        blank=True,
        null=True,
        unique=True,
        max_length=50    
    )
    
    picture = models.ImageField(
        _("profile picture"),
        default='profile/default_user.png',
        upload_to='profile', blank=True, null=True
    )
    
    bio = models.TextField(
        max_length=200,
        blank=True,
        
    )
    
    
    class Meta:
        verbose_name = _('user-profile')
        verbose_name_plural = _('user-profiles')

    def get_username(self):
        return self.username
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.picture.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.picture.path)
