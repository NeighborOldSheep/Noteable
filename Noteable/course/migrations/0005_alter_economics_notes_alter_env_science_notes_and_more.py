# Generated by Django 4.1.3 on 2022-11-19 04:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20221109_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economics',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='env_science',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='human_geography',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='psychology',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='world_history',
            name='notes',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
