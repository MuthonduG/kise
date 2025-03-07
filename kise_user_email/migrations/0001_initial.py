# Generated by Django 5.1.6 on 2025-03-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.CharField(max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
