from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator

class CustomerCompany(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įmonės pavadinimas pvz UAB "Terinta"')
    address = models.CharField('Adresas', max_length=200, help_text='Įmonės adresas registru sistemoje')
    VATcode = models.CharField('PVM kodas', max_length=200, help_text='Įmonės PVM moketojo kodas')
    companyCode = models.CharField('Imones kodas', max_length=200, help_text='Įmonės kodas')
    discountForCompany = models.CharField('Nuolaida imonei', max_length=200,
                                          help_text='Nuolaidos dydis taikomas imonei')

    class Meta:
        verbose_name = 'Imone kliente'
        verbose_name_plural = "Imones klientes"

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Imones pavadinimas')

    def display_store_items(self):
        return ', '.join(store_item.name for store_item in self.store_item.all()[:6])

    display_store_items.short_description = 'Tiekiamos prekes'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tiekejas'
        verbose_name_plural = "Tiekejai"


class StoreItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Pavadinimas', max_length=200, help_text='Prekes pavadinimas')
    price = models.FloatField('Kaina', help_text='Prekes kaina')
    description = models.TextField('Aprasymas', max_length=200, help_text='Prekes aprasymas')
    supplier = models.ManyToManyField(Supplier, null=True, help_text='parinkite galimus tiekejus siai prekei',
                                      related_name="store_item")

    picture = models.ImageField('Paveikslelis', help_text='ikelkite paveiksleli, geriausia, kad jo ratio butu 16:9',
                                upload_to='itemImages', null=True)
    created_at = models.DateTimeField('Sukurimo data', auto_now_add=True)
    updated_at = models.DateTimeField('Paskutini karta atnaujinta', auto_now=True)

    WEBSITE_SHOW = (
        (True, 'Rodyti'),
        (False, 'Nerodyti')
    )

    show = models.BooleanField('Rodyti tinklalapyje', max_length=1, choices=WEBSITE_SHOW, blank=True, default=False,
                               help_text='pasirinkti ar rodyti tinklalapyje (iskart nustatomas nerodyti')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produktas'
        verbose_name_plural = "Produktai"


class RecipesItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Pavadinimas', max_length=200, help_text="recepto pavadinimas")
    text = models.TextField('Recepto aprasymas', max_length=2000, help_text='Recepto aprasymas')
    picture = models.ImageField('Recepto paveikslelis',
                                help_text='ikelkite paveiksleli, geriausia, kad jo ratio butu 16:9',
                                upload_to='itemImages', null=True)

    products = models.ManyToManyField(StoreItem, help_text='parinkite prekes kurios ieina i si recepta',
                                      related_name="recipe_items", null=True)

    created_at = models.DateTimeField('Sukurimo data', auto_now_add=True)
    updated_at = models.DateTimeField('Paskutini karta atnaujinta', auto_now=True)

    WEBSITE_SHOW = (
        (True, 'Rodyti'),
        (False, 'Nerodyti')
    )

    def get_related_products(self):
        return "\n".join([p.name for p in self.products.all()])

    show = models.BooleanField('Rodyti tinklalapyje', max_length=1, choices=WEBSITE_SHOW, blank=True, default=False,
                               help_text='pasirinkti ar rodyti tinklalapyje (iskart nustatomas nerodyti')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Receptas"
        verbose_name_plural = "Receptai"


class WebsiteInfo(models.Model):
    backgroundImage = models.ImageField('Background paveikslelis', upload_to='websiteMainImages', null=True)

    name_field1 = models.CharField('Apie mus pastraipos pavadinimas', max_length=30,
                                   help_text="Pakeicia apie mus pastraipos pavadinima", default="Musu maistas")
    text_field1 = models.TextField('Pirmos temos tekstas', help_text='Pirmosios temos tekstas')

    contact_field = models.TextField('Mus Rasite tekstas', help_text='Tekstas po mus rasite skyrelio kontaktuose')

    google_maps_link = models.TextField('Google maps link', max_length=400,
                                        help_text='google maps zemelapio nuoroda(embed url)')
    facebook_page_link = models.CharField('Facebook page link', max_length=40,
                                          help_text='facebook puslapio nuoroda')

    # reikalingas, kad negaletum sukurt daugiau nei vieno instance sio objeckto
    def save(self, *args, **kwargs):
        if not self.pk and WebsiteInfo.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(WebsiteInfo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tinklapio duomenys'
        verbose_name_plural = "Tinklapio duomenys"


class Review(models.Model):
    name = models.CharField('Vardas', max_length=30)
    email = models.CharField('Elektroninis pastas', max_length=40,  blank=True,
                              validators=[EmailValidator(message="Įveskite teisingą elektroninio pašto adresą.")])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Telefonas turėtų būti įvestas formatu: '+xxxx'. Galima įvesti iki 15 skaičių.")
    phone_number = models.CharField('Telefono numeris', max_length=15,  blank=True, validators=[phone_regex],)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas')

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = "Atsiliepimai"