from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import ProductView, CategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', ProductView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('category/create/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', CategoryView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

