from django.contrib import admin

# Register your models here.

from .models import SD
from .models import BPMN

admin.site.register(SD)
admin.site.register(BPMN)