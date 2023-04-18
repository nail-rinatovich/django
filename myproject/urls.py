from django.urls import include, path
from django.contrib import admin
urlpatterns = [    
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Добавили новый маршрут
    path('accounts/', include('accounts.urls')),
    path('', include('myapp.urls')),
]
