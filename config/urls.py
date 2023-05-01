from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from eval import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eval/', include('eval.urls')),
    path('common/', include('common.urls')),
    path('', views.home, name='home'),  # '/' 에 해당되는 path
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

