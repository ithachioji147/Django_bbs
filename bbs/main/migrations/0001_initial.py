# Generated by Django 4.2.7 on 2023-12-12 01:43

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=40)),
                ('text', models.TextField(blank=True)),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='attachment/', validators=[main.models.validate_file_size])),
                ('status', models.CharField(blank=True, choices=[('DRAFT', '未承認'), ('APPROVED', '承認済'), ('DELETED', '削除済')], default='DRAFT', max_length=10)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('edited_datetime', models.DateTimeField(auto_now=True)),
                ('passcode', models.CharField(blank=True, max_length=4, null=True)),
                ('theme', models.ForeignKey(default='no_select', on_delete=django.db.models.deletion.DO_NOTHING, to='main.theme')),
            ],
        ),
    ]
