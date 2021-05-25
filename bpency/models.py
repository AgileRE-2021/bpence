from django.db import models
from django.db.models.base import Model

# Create your models here.
class SD(models.Model):
    code = models.TextField()

class BPMN(models.Model):
    api = models.TextField()