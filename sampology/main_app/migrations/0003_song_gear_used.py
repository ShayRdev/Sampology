# Generated by Django 4.2.1 on 2023-05-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gear'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='gear_used',
            field=models.ManyToManyField(to='main_app.gear'),
        ),
    ]