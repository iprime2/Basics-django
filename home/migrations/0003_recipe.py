# Generated by Django 4.2.4 on 2023-08-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_remove_student_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]
