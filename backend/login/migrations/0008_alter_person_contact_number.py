# Generated by Django 4.1.5 on 2023-01-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_person_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact_number',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
