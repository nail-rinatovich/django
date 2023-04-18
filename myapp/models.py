from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.urls import reverse
class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, null=False, default='test')
    class MPTTMeta:
        order_insertion_by = ['title', 'slug']

    class Meta:
        verbose_name_plural = "categories"
    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, blank=False)

    def __str__(self):
        return self.title
