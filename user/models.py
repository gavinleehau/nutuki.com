from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField('Họ Và tên',blank=False, max_length=30, default='')
    phone = models.CharField('Số điện thoại',blank=False, max_length=20)
    address = models.CharField('Địa chỉ',blank=True, max_length=150)
    city = models.CharField('Thành phố',blank=True, max_length=20)
    country = models.CharField('Quốc gia',blank=True, max_length=20)
    state = models.CharField('Trạng thái',blank=True, max_length=50)
    image = models.ImageField('Ảnh đại diện',blank=True, null=False, upload_to='images/users/')


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
