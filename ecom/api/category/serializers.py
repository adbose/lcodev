from rest_framework import serializers
from .models import Category


# if your viewset is inherited from ModelViewset,
# your serializer is should also inherit ModelSerializer
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
