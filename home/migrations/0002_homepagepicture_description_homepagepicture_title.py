# Generated by Django 4.0 on 2022-01-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagepicture',
            name='description',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homepagepicture',
            name='title',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
