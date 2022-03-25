from django.urls import path

from .views import HomePageView, AboutPageView # новое

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # новое
    path('', HomePageView.as_view(), name='home'),
]
