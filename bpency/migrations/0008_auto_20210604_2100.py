# Generated by Django 3.2.2 on 2021-06-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpency', '0007_auto_20210604_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userd',
            name='nama',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='userd',
            name='passw',
            field=models.CharField(max_length=256),
        ),
    ]