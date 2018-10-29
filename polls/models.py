from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.urls import reverse


# Create your models here.
class PollsType(models.Model):
    type_name=models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Polls(models.Model, ReadNumExpandMethod):
    title=models.CharField(max_length=50)
    polls_type=models.ForeignKey(PollsType, on_delete=models.CASCADE)
    content=RichTextUploadingField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    read_details=GenericRelation(ReadDetail)
    created_time=models.DateTimeField(auto_now=True)
    last_updated_time=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('polls_detail', kwargs={'polls_id': self.id})
  
    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<polls: %s>" % self.title

    class Meta:
        ordering=['-created_time']             #排序文章 新-->旧

'''class ReadNum(models.Model):
    read_num=models.IntegerField(default=0)
    polls=models.OneToOneField(Polls, on_delete=models.CASCADE)'''

