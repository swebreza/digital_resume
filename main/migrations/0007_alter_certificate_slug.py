# Generated by Django 3.2.8 on 2021-11-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_certificate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
