# Generated by Django 4.2.7 on 2023-11-28 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_article_passcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url_link',
        ),
    ]
