# Generated by Django 2.1.5 on 2019-03-08 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190308_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='link_site',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
