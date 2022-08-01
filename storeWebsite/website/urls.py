from django.urls import path

from . import views

urlpatterns = [
    path('items/', views.StoreItemListView.as_view(), name='store_items'),
    path('index/', views.IndexView.as_view(), name='index'),

]
