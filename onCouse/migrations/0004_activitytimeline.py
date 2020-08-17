# Generated by Django 3.1 on 2020-08-09 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onCouse', '0003_auto_20200809_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_start', models.DateTimeField()),
                ('activity_stop', models.DateTimeField(blank=True, null=True)),
                ('activity_plantitle', models.CharField(max_length=255)),
                ('onCouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onCouse.onCouse')),
            ],
        ),
    ]