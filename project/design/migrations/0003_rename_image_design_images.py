# Generated by Django 4.2.8 on 2023-12-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_remove_design_images_design_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='image',
            new_name='images',
        ),
    ]
