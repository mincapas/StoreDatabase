from django.urls import path

from . import views

urlpatterns = [
    path('items/<int:pk>', views.SingleStoreItemView.as_view(), name='single_store_item'),
    path('recipes/<int:pk>', views.SingleRecipeView.as_view(), name='single_recipe'),
    path('atsiliepimai/', views.ContactView.as_view(), name='review'),
    path('atsiliepimai/aciu/', views.ThanksView.as_view(), name='thanks'),
    path('apiemus/', views.AboutUsView.as_view(), name='about'),
    path('index/', views.IndexView.as_view(), name='index'),


]
