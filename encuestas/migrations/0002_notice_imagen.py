# Generated by Django 4.0.6 on 2022-08-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='imagen',
            field=models.ImageField(null=True, upload_to='noticias'),
        ),
    ]
