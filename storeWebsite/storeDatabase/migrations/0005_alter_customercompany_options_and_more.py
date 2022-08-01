# Generated by Django 4.0.6 on 2022-07-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0004_storeitem_show'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customercompany',
            options={'verbose_name': 'Imone kliente', 'verbose_name_plural': 'Imones klientes'},
        ),
        migrations.AlterModelOptions(
            name='storeitem',
            options={'verbose_name': 'Produktas', 'verbose_name_plural': 'Produktai'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Tiekejas', 'verbose_name_plural': 'Tiekejai'},
        ),
        migrations.AlterField(
            model_name='storeitem',
            name='supplier',
            field=models.ManyToManyField(help_text='parinkite galimus tiekejus siai prekei', related_name='store_item', to='storeDatabase.supplier'),
        ),
    ]