# Generated by Django 4.1.3 on 2023-01-23 04:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_question_explain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=ckeditor.fields.RichTextField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10, verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='question',
            name='explain',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='题目解析'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionA',
            field=ckeditor.fields.RichTextField(max_length=258, verbose_name='A选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionB',
            field=ckeditor.fields.RichTextField(max_length=258, verbose_name='B选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionC',
            field=ckeditor.fields.RichTextField(max_length=258, verbose_name='C选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionD',
            field=ckeditor.fields.RichTextField(max_length=258, verbose_name='D选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionE',
            field=ckeditor.fields.RichTextField(default='', max_length=258, verbose_name='E选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=ckeditor.fields.RichTextField(verbose_name='题目'),
        ),
    ]