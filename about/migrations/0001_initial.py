# Generated by Django 4.0 on 2021-12-28 12:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infoCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100, verbose_name='Tên công ty')),
                ('MST', models.CharField(max_length=20, null=True, verbose_name='Mã số thuế')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo')),
                ('founding', models.DateField(null=True, verbose_name='Ngày thành lập')),
                ('faceBook', models.CharField(max_length=100, null=True, verbose_name='Facebook')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email')),
                ('phoneNumber', models.CharField(max_length=11, verbose_name='Số điện thoại')),
                ('address', models.CharField(max_length=100, verbose_name='Địa chỉ')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mô tả')),
            ],
            options={
                'db_table': 'info company',
            },
        ),
    ]
