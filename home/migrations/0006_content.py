# Generated by Django 4.0 on 2022-01-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_testimonial_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('gallery_title', models.CharField(max_length=254)),
                ('gallery_text', models.CharField(max_length=254)),
                ('video_title', models.CharField(max_length=254)),
                ('video_text', models.CharField(max_length=254)),
                ('testimonial_title', models.CharField(max_length=254)),
                ('testimonial_text', models.CharField(max_length=254)),
            ],
        ),
    ]
