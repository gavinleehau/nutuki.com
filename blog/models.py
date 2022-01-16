from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django import forms
import datetime
from django.utils import timezone


# Create your models here.
class article(models.Model):
  title = models.CharField('Tiêu đề', max_length=1000)
  date = models.DateTimeField('ngày đăng')
  avata = models.ImageField('ảnh đại chủ đề')
  content = RichTextUploadingField('Nội dung')

  def __str__(self):
      return self.title

  # def avaregereview(self):
  #       reviews = Comment.objects.filter(article=self, status='New').aggregate(avarage=models.Avg('rate'))
  #       avg = 0
  #       if reviews["avarage"] is not None:
  #           avg = float(reviews["avarage"])
  #       return avg

  class Meta:
    ordering = ['-id']
    db_table = 'article'

class InstagramFeeds(models.Model):
  note = models.CharField('Note', max_length=100, default='Ảnh instagram')
  image = models.ImageField('ảnh instagram feeds')

  def __str__(self):
    return self.note

class Comment(models.Model):
  article = models.ForeignKey(article,on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  subject = models.CharField(max_length=50, blank=True, null=True)
  comment = models.CharField(max_length=250,blank=True, null=True)
  create_at = models.DateTimeField('thơi gian đăng', null=True, default=timezone.now)
  update_at = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return str(self.subject)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['subject', 'comment']
    widgets = { 
      'comment' : forms.Textarea(attrs={'class':'form-control w-100'})
    }

	

