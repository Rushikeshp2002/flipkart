# Generated by Django 4.2.4 on 2023-08-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='education',
        ),
        migrations.AddField(
            model_name='signup',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]