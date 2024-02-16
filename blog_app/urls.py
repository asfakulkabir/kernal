from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog_page/', views.blog_page, name='blog_page'),
    path('blog_post/<str:slug>/' , views.blog_post , name="blog_post"),
    path('blog_post/category/<str:slug>/' , views.blog_post_category , name="blog_post_category "),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)