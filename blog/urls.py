# blog/urls.py
from django.urls import path, include
from django.contrib import admin
from blog.views import CategoryListView, PostByCategoryView
from django.conf.urls.static import static
from django.conf import settings # new
from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView, # Импортируем представление

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    #path('', BlogListView.as_view(), name='home'),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
    ]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
