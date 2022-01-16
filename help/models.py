from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Questions(models.Model):
	question = models.CharField("Câu Hỏi: ",max_length=200, null=False)
	answer = RichTextUploadingField("Câu trả lời: ",default="",null=True)


	def __str__(self):
		return self.question

	class Meta:
		ordering = ['-id']
		db_table = "qustions"


