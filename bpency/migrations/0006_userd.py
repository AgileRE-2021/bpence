# Generated by Django 3.2.2 on 2021-06-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpency', '0005_alter_sd_iduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='userD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=256)),
            ],
        ),
    ]
