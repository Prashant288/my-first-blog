# Generated by Django 2.1.5 on 2019-04-27 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
