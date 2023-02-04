from django.db import models
from ckeditor.fields import RichTextField




# Create your models here.
class Question(models.Model):

    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E')
    )
   
    subject = models.CharField('科目', max_length=20)
    title = RichTextField('题目')
    optionA = RichTextField('A选项')
    optionB = RichTextField('B选项')
    optionC = RichTextField('C选项')
    optionD = RichTextField('D选项')
    optionE = RichTextField('E选项',default='')
    answer = RichTextField('答案',max_length=10,choices=ANSWER)
    explain = RichTextField("题目解析",blank=True)

    class Meta:
        db_table='question'
        verbose_name='单项选择题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title)