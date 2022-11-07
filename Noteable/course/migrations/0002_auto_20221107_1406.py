# Generated by Django 3.1.4 on 2022-11-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economics',
            name='info',
        ),
        migrations.RemoveField(
            model_name='env_science',
            name='info',
        ),
        migrations.RemoveField(
            model_name='human_geography',
            name='info',
        ),
        migrations.RemoveField(
            model_name='psychology',
            name='info',
        ),
        migrations.RemoveField(
            model_name='seminar',
            name='info',
        ),
        migrations.RemoveField(
            model_name='world_history',
            name='info',
        ),
        migrations.AlterField(
            model_name='economics',
            name='notes',
            field=models.TextField(max_length=288),
        ),
        migrations.AlterField(
            model_name='env_science',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='human_geography',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='psychology',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='world_history',
            name='notes',
            field=models.TextField(),
        ),
    ]