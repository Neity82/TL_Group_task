# Generated by Django 3.2.15 on 2022-10-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20221028_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['is_chief', 'full_name'], 'verbose_name': 'employee', 'verbose_name_plural': 'employees'},
        ),
    ]
