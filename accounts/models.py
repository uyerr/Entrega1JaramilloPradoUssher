from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtensionUsuario(models.Model):
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True)
    website = models.URLField(max_length=100, null=True)
    avatar = models.ImageField(upload_to='avatar' ,null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'