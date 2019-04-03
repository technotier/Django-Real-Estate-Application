# Generated by Django 2.1.7 on 2019-03-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('fb_link', models.URLField()),
                ('insta_link', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
    ]