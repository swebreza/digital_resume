# Generated by Django 3.2.8 on 2021-11-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_certificate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
