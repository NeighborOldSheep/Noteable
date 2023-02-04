# Generated by Django 4.1.3 on 2023-02-02 17:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_alter_question_answer_alter_question_explain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='optionA',
            field=ckeditor.fields.RichTextField(verbose_name='A选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionB',
            field=ckeditor.fields.RichTextField(verbose_name='B选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionC',
            field=ckeditor.fields.RichTextField(verbose_name='C选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionD',
            field=ckeditor.fields.RichTextField(verbose_name='D选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionE',
            field=ckeditor.fields.RichTextField(default='', verbose_name='E选项'),
        ),
    ]
