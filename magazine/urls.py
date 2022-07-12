from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import ProductView, CategoryView
from costum_auth.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', ProductView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('category/create/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('category/create/<int:pk>/', CategoryView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

