# Generated by Django 4.0.3 on 2022-04-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_image_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='labels',
            field=models.CharField(choices=[('NEW', 'New'), ('BEST', 'BEST'), ('RECENT', 'Recent')], default='RECENT', max_length=6),
        ),
    ]
