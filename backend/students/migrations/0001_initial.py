# Generated by Django 4.1.5 on 2023-01-17 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.SmallIntegerField(null=True)),
                ('certificate', models.ImageField(upload_to='')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.person')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.tests')),
            ],
            options={
                'db_table': 'Test_Scores',
            },
        ),
        migrations.CreateModel(
            name='Accessed_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_num', models.PositiveSmallIntegerField(null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.person')),
            ],
            options={
                'db_table': 'Accessed_Course',
            },
        ),
    ]
