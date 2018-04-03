# Generated by Django 2.0.4 on 2018-04-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='動画タイトル')),
                ('description', models.TextField(blank=True, verbose_name='説明(空欄可)')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='サムネイル')),
                ('upload', models.FileField(upload_to='uploads/%y/%m/%d/', verbose_name='ファイル')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
