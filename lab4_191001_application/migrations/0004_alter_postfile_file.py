# Generated by Django 4.0.5 on 2022-06-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab4_191001_application', '0003_rename_file_postfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]