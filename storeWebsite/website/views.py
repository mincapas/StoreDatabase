from django.shortcuts import render
from django.http import HttpResponse
from storeDatabase.models import StoreItem, WebsiteInfo, RecipesItem

# paprastiems class views paveldejimams
from django.views import generic


class IndexView(generic.TemplateView):
    # prekiu skaicius
    template_name = "index.html"

    # website duomenys kontaktams. labai svarbu kad websiteInfo tik vienas objektas butu
    def get_contact_us_as_list_for_jinja(self):
        for item in WebsiteInfo.objects.all():
            lines = item.contact_field.splitlines()
        return lines

    def get_website_info(self):
        for item in WebsiteInfo.objects.all():
            return item;

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['websiteinfo'] = self.get_website_info()
        context['storeitems'] = StoreItem.objects.filter(show=True)
        context['recipeitems'] = RecipesItem.objects.filter(show=True)
        context['contact_us']  = self.get_contact_us_as_list_for_jinja()
        return context


class StoreItemListView(generic.ListView):
    model = StoreItem
    template_name = 'store_item_list.html'
