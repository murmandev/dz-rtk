# Generated by Django 4.2.6 on 2023-12-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_account_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужчина'), ('F', 'Женщина'), ('N/A', 'Не определился')], max_length=20, null=True, verbose_name='Пол'),
        ),
    ]
