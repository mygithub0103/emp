# Generated by Django 4.2 on 2025-02-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
                ('legs', models.FloatField()),
            ],
        ),
    ]
