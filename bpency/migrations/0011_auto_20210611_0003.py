# Generated by Django 3.2.2 on 2021-06-10 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bpency', '0010_alter_bpmn_idsd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bpmn',
            name='idSD',
        ),
        migrations.RemoveField(
            model_name='sd',
            name='idUser',
        ),
    ]
