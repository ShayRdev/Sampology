# Generated by Django 4.2.1 on 2023-05-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_name', models.CharField(max_length=100)),
                ('gear_brand', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]
