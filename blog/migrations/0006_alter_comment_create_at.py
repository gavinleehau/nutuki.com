# Generated by Django 3.2.7 on 2022-01-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(null=True, verbose_name='thơi gian đăng'),
        ),
    ]