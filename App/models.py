from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Drive(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    file = models.FileField(upload_to='userfiles/%y/%m/%d',null=False,blank=False)
    name = models.CharField(max_length=1000,null=False,blank=False)
    extension = models.CharField(max_length=40,null=False,blank=False,editable=False)
    size = models.IntegerField(null=False,blank=False,editable=False)
    uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
