# Generated by Django 4.2.3 on 2023-07-20 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_table2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table2',
            old_name='img',
            new_name='timg',
        ),
        migrations.RenameField(
            model_name='table2',
            old_name='name',
            new_name='tname',
        ),
    ]
