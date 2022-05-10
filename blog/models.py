from django.db import models
from django.urls import reverse # Новый импорт

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')

# Модель статья
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    # другие поля ....

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])
