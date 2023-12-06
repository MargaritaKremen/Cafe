from django.urls import path
from .views import AllItemsView, AllCategoriesView, ItemDetailView, CategoryItemsDetailView, CategoryList

urlpatterns = [
    path('', AllItemsView.as_view(), name='all-items'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('category-items/', CategoryList.as_view(), name='category-items'),
    path('category-items/<int:pk>/', CategoryItemsDetailView.as_view(), name='category-items-detail'),
    path('all-categories/', AllCategoriesView.as_view(), name='all-categories'),
]