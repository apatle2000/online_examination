# Generated by Django 4.1.5 on 2023-01-17 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_person_middle_name_alter_person_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
