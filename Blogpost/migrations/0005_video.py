# Generated by Django 2.2.7 on 2020-01-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogpost', '0004_blogpost_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]