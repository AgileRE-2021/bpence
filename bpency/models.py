from django.db import models
from django.db.models.base import Model

# Create your models here.
class userD(models.Model):
    nama = models.CharField(max_length=256)
    email = models.EmailField(max_length=50)
    passw = models.CharField(max_length=256)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)

class SD(models.Model):
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return "{}. {}".format(self.code)

class BPMN(models.Model):
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #def __str__(self):
    #    return "{}. {}".format(self.code)