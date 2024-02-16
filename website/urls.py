from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import product

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('product/<str:slug>/' , views.product , name="product"),
    path('cart/' , views.cart , name="cart"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)