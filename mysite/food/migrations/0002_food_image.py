# Generated by Django 4.0 on 2024-04-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.CharField(default='https://www.foodista.com/sites/default/files/default_images/placeholder_rev.png', max_length=600),
        ),
    ]