# Generated by Django 4.0.5 on 2022-06-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab4_191001_application', '0007_postfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.DeleteModel(
            name='PostFile',
        ),
    ]
