# Generated by Django 3.2.2 on 2021-06-10 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpency', '0009_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpmn',
            name='idSD',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='bpency.sd'),
        ),
    ]
