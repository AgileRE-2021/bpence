from django.contrib import admin

# Register your models here.
from .models import SD, BPMN, userD

admin.site.register(SD)
admin.site.register(BPMN)
admin.site.register(userD)