from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	user_image = models.ImageField(default='')
	feedback = RichTextUploadingField("feedback: ", default="",null=True)


	def __str__(self):
		return str(self.user)

	class Meta:
		ordering = ['-id']
		db_table = "feedback"

class heroDemo(models.Model):
	title = models.CharField('tiêu đề hero', max_length=100)
	subTitle = models.CharField('tiêu đề nhỏ', max_length=100)
	content = models.CharField('nội dung here', max_length=200)

	def __str__(self):
		return self.title

	class Meta:
		db_table = "Demo Hero"
					



				