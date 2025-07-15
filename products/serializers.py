# products/serializers.py

from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    '''
    Serializador para o modelo Category
    '''
    class Meta:
        model = Category
        fields = '__all__' # Inclui todos os campos do modelo Category 


class ProductSerializer(serializers.ModelSerializer):
    '''
    Serializador para o modelo Product
    '''
    class Meta:
        model = Product
        fields = '__all__' # Inclui todos os campos do modelo Product
        