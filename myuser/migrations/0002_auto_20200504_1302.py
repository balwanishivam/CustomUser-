# Generated by Django 3.0.4 on 2020-05-04 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='usrname',
            new_name='username',
        ),
    ]
