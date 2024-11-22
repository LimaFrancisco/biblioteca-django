from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CollectionViewSet
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'collections', CollectionViewSet, basename='collection')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
