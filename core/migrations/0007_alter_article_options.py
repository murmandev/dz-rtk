# Generated by Django 4.2.6 on 2023-12-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_article_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date', 'title'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
