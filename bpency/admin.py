from django.contrib import admin

# Register your models here.
from .models import user, SD, BPMN

admin.site.register(user)
admin.site.register(SD)
admin.site.register(BPMN)