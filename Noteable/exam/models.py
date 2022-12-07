from django.db import models


Type = (
    (0, '单选'),
    (1, '多选')
)
 
Option = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E')
)
 
# Create your models here.
class Subject(models.Model):
    stem = models.CharField(max_length=1024, verbose_name='题干内容', blank=False, null=False)
    type = models.IntegerField(choices=Type, verbose_name='题目类型,单选还是多选')
    
 
    class Meta:
        db_table = 'subject'
        verbose_name = '题库'
 
class Options(models.Model):
    options = models.IntegerField(choices=Option, verbose_name='选项ABCDEFGH')
    content = models.CharField(max_length=256, verbose_name='选项内容')
    subject = models.ForeignKey('Subject',on_delete = models.CASCADE)
 
    class Meta:
        db_table = 'options'
        verbose_name = '选项表'
        unique_together = ('subject', 'content')
        ordering = ['options']
 
class Answer(models.Model):
    options = models.IntegerField(choices=Option, verbose_name='正确答案ABCDEFGH')
    subject = models.ForeignKey('Subject',on_delete = models.CASCADE)
 
    class Meta:
        db_table = 'answer'
        verbose_name = '答案表'
        unique_together = ('subject', 'options')
        ordering = ['options']