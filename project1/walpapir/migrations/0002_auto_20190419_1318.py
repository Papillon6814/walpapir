# Generated by Django 2.1.4 on 2019-04-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walpapir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='walpapir_style')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='profilepicture',
            field=models.ImageField(default='profile_image/180x120.jpeg', upload_to='profile_image'),
        ),
    ]
