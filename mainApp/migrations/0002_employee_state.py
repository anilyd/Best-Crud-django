# Generated by Django 5.0.1 on 2024-01-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]