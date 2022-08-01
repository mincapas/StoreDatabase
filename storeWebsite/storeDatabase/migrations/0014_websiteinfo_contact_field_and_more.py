# Generated by Django 4.0.6 on 2022-07-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0013_rename_publications_recipesitem_related_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinfo',
            name='contact_field',
            field=models.TextField(default='laikina', help_text='Tekstas po mus rasite skyrelio kontaktuose', verbose_name='Mus Rasite tekstas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websiteinfo',
            name='google_maps_link',
            field=models.CharField(default='laikina', help_text='google maps zemelapio nuoroda(embed url)', max_length=200, verbose_name='Google maps link'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipesitem',
            name='show',
            field=models.BooleanField(blank=True, choices=[(True, 'Rodyti'), (False, 'Nerodyti')], default=False, help_text='pasirinkti ar rodyti tinklalapyje (iskart nustatomas nerodyti', max_length=1, verbose_name='Rodyti tinklalapyje'),
        ),
        migrations.AlterField(
            model_name='storeitem',
            name='show',
            field=models.BooleanField(blank=True, choices=[(True, 'Rodyti'), (False, 'Nerodyti')], default=False, help_text='pasirinkti ar rodyti tinklalapyje (iskart nustatomas nerodyti', max_length=1, verbose_name='Rodyti tinklalapyje'),
        ),
    ]
