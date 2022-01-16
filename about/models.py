from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class infoCompany(models.Model):
  companyName = models.CharField('Tên công ty', max_length=100)
  MST = models.CharField('Mã số thuế', null=True, max_length=20)
  logo = models.ImageField('Logo')
  founding = models.DateField('Ngày thành lập', null=True)
  faceBook = models.CharField('Facebook', null=True, max_length=100)
  email = models.CharField('Email', null=True, max_length=100)
  phoneNumber = models.CharField('Số điện thoại', max_length=11)
  address = models.CharField('Địa chỉ', max_length=100)
  location = models.CharField('Thành phố / Tỉnh',null=True, max_length=100)
  description = RichTextUploadingField('Mô tả')

  def __str__(self):
    return self.companyName
  
  class Meta:
    db_table = 'info company'
          