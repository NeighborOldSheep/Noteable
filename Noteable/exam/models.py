from django.db import models



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
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length = 258)
    optionB=models.CharField('B选项',max_length = 258)
    optionC=models.CharField('C选项',max_length = 258)
    optionD=models.CharField('D选项',max_length = 258)
    optionE=models.CharField('E选项',max_length = 258, default='')
    answer=models.CharField('答案',max_length=10,choices=ANSWER)
    class Meta:
        db_table='question'
        verbose_name='单项选择题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title)