from rest_framework import serializers
from .models import Papers, Subjects


class Paperserializer(serializers.ModelSerializer):

    class Meta:
        model = Papers
        fields = ['id', 'title', 'thumbnail', 'file', 'get_file',
                  'subject', 'get_absolute_url']


class Subjectserializer(serializers.ModelSerializer):
    papers = Paperserializer(many=True)

    class Meta:
        model = Subjects
        fields = ['id', 'title', 'get_image',
                  'get_thumbnail', 'get_absolute_url', 'papers']


class Subjectsserializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'title', 'image', 'get_image',
                  'get_thumbnail', 'get_absolute_url']
