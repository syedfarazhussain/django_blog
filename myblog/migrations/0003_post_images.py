# Generated by Django 3.0.7 on 2020-10-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20201022_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
