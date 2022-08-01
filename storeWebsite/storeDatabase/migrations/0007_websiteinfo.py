# Generated by Django 4.0.6 on 2022-07-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0006_alter_storeitem_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_field1', models.CharField(default='Musu maistas', help_text='pakeicia virsutinio lango pavadinimas', max_length=30, verbose_name='Pirmos pastraipos pavadinimas')),
                ('text_field1', models.TextField(help_text='Pirmosios temos tekstas', verbose_name='Pirmos temos tekstas')),
            ],
            options={
                'verbose_name': 'Tinklapio duomenys',
                'verbose_name_plural': 'Tinklapio duomenys',
            },
        ),
    ]
