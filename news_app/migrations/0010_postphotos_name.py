# Generated by Django 5.0.1 on 2024-02-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0009_remove_post_main_image_alter_post_image_postphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphotos',
            name='name',
            field=models.CharField(blank=True, max_length=350, verbose_name='Название'),
        ),
    ]
