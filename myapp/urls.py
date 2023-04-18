from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete

from .views import CategoryListView
from .views import PostByCategoryView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/update/', post_update, name='post_update'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]
