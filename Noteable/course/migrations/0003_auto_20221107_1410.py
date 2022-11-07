# Generated by Django 3.1.4 on 2022-11-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20221107_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='economics',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AddField(
            model_name='env_science',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AddField(
            model_name='human_geography',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AddField(
            model_name='psychology',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AddField(
            model_name='seminar',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AddField(
            model_name='world_history',
            name='intro',
            field=models.CharField(default='', max_length=288),
        ),
        migrations.AlterField(
            model_name='economics',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='env_science',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='human_geography',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='psychology',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='world_history',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]