from django.db import models
from django.db.models.base import Model

# Create your models here.
class user(models.Model):
    nama = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    passw = models.CharField(max_length=12)

class SD(models.Model):
    idUser = models.CharField(max_length=12, default='2')
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.code)

class BPMN(models.Model):
    idSD = models.ForeignKey(SD, on_delete=models.CASCADE)
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)