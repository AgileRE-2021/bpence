# Generated by Django 3.2.2 on 2021-06-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpency', '0006_userd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userd',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userd',
            name='nama',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='userd',
            name='passw',
            field=models.CharField(max_length=12),
        ),
    ]