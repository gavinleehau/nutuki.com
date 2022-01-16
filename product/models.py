from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class website(models.Model):
  storage_options = (('500_MB' ,'500 MB'), ('1_GB' ,'1 GB'), ('2_GB' ,'2 GB'), ('5_GB' ,'5 GB'))
  freeDomain_options = (('Yes','Yes'), ('No','No'))
  template_options = (('Theo mẫu','Theo mẫu'), ('Theo yêu cầu','Theo yêu cầu'))

  name = models.CharField('Tên gói', max_length=100)
  storage = models.CharField('Dung lượng', choices=storage_options, max_length=10)
  bandwidth = models.CharField('Dung lượng', max_length=100, default='Không giới hạn băng thông')
  freeDomain = models.CharField('Miễn phí domain', choices=freeDomain_options, max_length=3)
  template = models.CharField('Giao diện website', choices=template_options, max_length=20)
  descriptions = RichTextUploadingField('Mô tả', default='')
  old_pricing = models.DecimalField('Giá tiền cũ',max_digits=100, decimal_places=0, null=True)
  pricing = models.DecimalField('Giá tiền',max_digits=100, decimal_places=0)

  class Meta:
    db_table = 'website'

  def __str__(self):
      return self.name

class emailBusiness(models.Model):
  shareDrive_options = (('Yes','Yes'),('No','No'))
  storage_options = (('30_GB' ,'30 GB'), ('2_TB' ,'2 TB'), ('5_TB' ,'5 TB'), ('Unlimited','Unlimited'))
  

  supplier = models.CharField('Nhà cung cấp', max_length=100)
  name = models.CharField('Tên gói', max_length=100)
  storage = models.CharField('Dung lượng', choices=storage_options, max_length=20)
  shareDrive = models.CharField('Drive nhóm', choices=shareDrive_options, max_length=3)
  descriptions = RichTextUploadingField('Mô tả', default='')
  old_pricing = models.DecimalField('Giá tiền cũ',max_digits=100, decimal_places=0, null=True)
  pricing = models.DecimalField('Giá tiền',max_digits=100, decimal_places=0)
  

  class Meta:
    db_table = 'email business'
  def __str__(self):
      return self.name
# class Domain(models.Model):

class Checkout(models.Model):
  oder_status = (('unfinished', 'Chưa hoàn thành'), ('finished', 'Hoàn thành'))
  
  selected_package = models.ForeignKey(website, on_delete=models.CASCADE, null=True)
  name = models.CharField("Họ tên: ", max_length=50, null=True)
  email = models.CharField("Email: ", max_length=100, null=True)
  phone = models.CharField("Số điện thoại: ", max_length=12, null=True)
  message = models.TextField("Nội dung", null=True)
  oderstatus = models.CharField('Trạng thái đơn hàng', choices=oder_status, max_length=20, default='')

  class meta:
    odering = ['-id']
    db_table = "checkout"

  def __str__(self):
    return str(self.name)


class Checkout_email(models.Model):
  # used_time = (('12','12 tháng'),('24','24 tháng'),('36','36 tháng'),('48','48 tháng'),('60','60 tháng'))
  oder_status = (('unfinished', 'Chưa hoàn thành'), ('finished', 'Hoàn thành'))

  selected_email_package = models.ForeignKey(emailBusiness, on_delete=models.CASCADE, null=True)
  name_domain = models.CharField("Tên miền đăng ký: ", max_length=100, null=True)
  used_time = models.CharField("Thời gian sử dụng: ", max_length=20)
  number_of_users = models.CharField("Số lượng người dùng: ", max_length=12, null=True)
  oderstatus = models.CharField('Trạng thái đơn hàng', choices=oder_status, max_length=20, default='')

  class meta:
    odering = ['-id']
    db_table = "Checkout Eemail Business"

  def __str__(self):
    return str(self.name_domain)


        
          
  


        
          
        