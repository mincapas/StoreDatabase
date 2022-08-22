from django.shortcuts import render
from django.http import HttpResponse
from storeDatabase.models import StoreItem, WebsiteInfo, RecipesItem
from website.forms import ContactForm
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# paprastiems class views paveldejimams
from django.views import generic


class BaseViewFunctions():
    # website duomenys kontaktams. labai svarbu kad websiteInfo tik vienas objektas butu
    def get_contact_us_as_list_for_jinja(self):
        for item in WebsiteInfo.objects.all():
            lines = item.contact_field.splitlines()
        return lines

    def get_website_info(self):
        for item in WebsiteInfo.objects.all():
            return item;


class IndexView(generic.TemplateView, BaseViewFunctions):
    # prekiu skaicius
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['storeitems'] = StoreItem.objects.filter(show=True)
        context['recipeitems'] = RecipesItem.objects.filter(show=True)
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        return context


class SingleStoreItemView(generic.DetailView, BaseViewFunctions):
    model = StoreItem
    template_name = "specific_product.html"

    def get_context_data(self, **kwargs):
        context = super(SingleStoreItemView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        context['recipe_items'] = RecipesItem.objects.filter(products__pk=self.object.id)
        return context


class SingleRecipeView(generic.DetailView, BaseViewFunctions):
    model = RecipesItem
    template_name = "specific_recipe.html"

    def get_context_data(self, **kwargs):
        context = super(SingleRecipeView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        context['store_items'] = StoreItem.objects.filter(recipe_items__pk=self.object.id)
        return context


class ContactView(generic.FormView, BaseViewFunctions):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'aciu/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        content = request.POST['content']
        message = 'Telefono numeris:' + phone_number + '\n' \
                  'žinutė: '+ content
        if form.is_valid():

            form.save()
            send_mail(
                name,
                message,
                email,
                ['test@test.com'],
                fail_silently=False,
            )
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        print("aasdadasdasd")
        return context


class ThanksView(generic.TemplateView, BaseViewFunctions):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        return context


class AboutUsView(generic.TemplateView, BaseViewFunctions):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['contact_us'] = self.get_contact_us_as_list_for_jinja()
        return context
