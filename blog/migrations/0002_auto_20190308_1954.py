# Generated by Django 2.1.5 on 2019-03-08 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contents',
            old_name='Textarea',
            new_name='textarea',
        ),
        migrations.RenameField(
            model_name='contents',
            old_name='Title',
            new_name='title',
        ),
    ]
