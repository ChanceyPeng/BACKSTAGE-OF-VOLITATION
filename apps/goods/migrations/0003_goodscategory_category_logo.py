# Generated by Django 2.2.3 on 2020-01-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191204_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='category_logo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='category_logo/'),
        ),
    ]