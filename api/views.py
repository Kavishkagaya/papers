from django.shortcuts import get_object_or_404
from .models import Subjects, Papers
from django.http import *
from .serializers import Subjectserializer, Paperserializer, Subjectsserializer
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .permissions import AllStaffAllcanEditANDuserReadOnly


# fastest method (modelviewset)
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = Subjectserializer
    permission_classes = [AllStaffAllcanEditANDuserReadOnly]
    authentication_classes = {TokenAuthentication, SessionAuthentication}

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        print(item)
        return get_object_or_404(Subjects, title=item)


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = Subjectsserializer
    permission_classes = [AllStaffAllcanEditANDuserReadOnly]
    authentication_classes = {TokenAuthentication, SessionAuthentication}


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = Paperserializer
    permission_classes = [AllStaffAllcanEditANDuserReadOnly]
    authentication_classes = {TokenAuthentication, SessionAuthentication}

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Papers, slug=item)
