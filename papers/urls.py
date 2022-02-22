from django.contrib import admin
from django.urls import path, include
from api.views import SubjectViewSet, PaperViewSet, SubjectsViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subject', SubjectViewSet, basename='subject')
router.register('subjects', SubjectsViewSet, basename='subjects')
router.register('papers', PaperViewSet, basename='papers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
] + static('/staticfiles/', document_root = settings.BASE_DIR + '/staticfiles/')
