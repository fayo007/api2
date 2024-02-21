from rest_framework import serializers
from main import models


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['image',]


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id',]

class DetailProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = models.Product
        depth = 1
        fields = ['id', 'name', 'description', 
                  'quantity', 'price', 'currency', 
                  'discount_price', 'baner_image', 
                  'category', 'review', 'is_discount', 
                  'is_active', 'images']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'