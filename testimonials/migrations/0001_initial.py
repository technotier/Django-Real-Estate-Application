# Generated by Django 2.1.7 on 2019-03-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=200)),
                ('partner_logo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('designation', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
