# Generated by Django 2.1.2 on 2018-10-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20181024_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['-views'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
