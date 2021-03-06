from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    subject = models.CharField(max_length=15)
    filetype = models.CharField(max_length=15)
    notesfile = models.FileField (null=True)
    role = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.subject