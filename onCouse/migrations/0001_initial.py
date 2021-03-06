# Generated by Django 3.1 on 2020-08-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255)),
                ('activity_type', models.CharField(choices=[('AC', 'ACADEMIC'), ('SA', 'STUDENT AFFAIR'), ('CU', 'CULTURAL')], max_length=2)),
                ('activity_desc', models.TextField(blank=True, null=True)),
                ('activity_date', models.DateField()),
            ],
        ),
    ]
