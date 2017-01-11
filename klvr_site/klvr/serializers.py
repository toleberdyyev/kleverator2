from rest_framework import serializers
from django.contrib.auth.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =  '__all__';