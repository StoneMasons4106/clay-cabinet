# Generated by Django 4.0 on 2022-01-18 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='testimonal',
            new_name='testimonial',
        ),
    ]
