from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Category, Item, Order


class CategoryList(ListView):
    model = Category
    template_name = 'cafe/category_items.html'
    context_object_name = 'categories'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'cafe/item_detail.html'
    context_object_name = 'item'


class AllItemsView(ListView):
    model = Item
    template_name = 'cafe/all_items.html'
    context_object_name = 'items'


class CategoryItemsDetailView(DetailView):
    model = Category
    template_name = 'cafe/category_items_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        items = Item.objects.filter(category=category)
        context['items'] = items
        return context


class AllCategoriesView(ListView):
    model = Category
    template_name = 'cafe/all_categories.html'
    context_object_name = 'categories'
# <h2><a href="{% url 'category-items' %}">{{ category.name }}</a></h2>