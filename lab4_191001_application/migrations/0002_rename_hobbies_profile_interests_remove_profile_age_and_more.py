# Generated by Django 4.0.5 on 2022-06-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab4_191001_application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hobbies',
            new_name='interests',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
