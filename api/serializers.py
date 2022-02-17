from rest_framework import serializers
from .models import Papers, Subjects


class Paperserializer(serializers.ModelSerializer):

    class Meta:
        model = Papers
        fields = ['id', 'title', 'imgurl', 'fileurl',
                  'subject', 'get_absolute_url']


class Subjectserializer(serializers.ModelSerializer):
    papers = Paperserializer(many=True)

    class Meta:
        model = Subjects
        fields = ['id', 'title', 'imgurl', 'get_absolute_url', 'papers']


class Subjectsserializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'title', 'imgurl', 'get_absolute_url']
