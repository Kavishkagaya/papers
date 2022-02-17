from django.contrib import admin
from django.urls import path, include
from api.views import SubjectViewSet, PaperViewSet, SubjectsViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('subject', SubjectViewSet, basename='subject')
router.register('subjects', SubjectsViewSet, basename='subjects')
router.register('papers', PaperViewSet, basename='papers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]
