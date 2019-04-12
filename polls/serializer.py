from .models import Product,Brand, ProductCategory,Product_Models,Variant, FeatureMaster, Feature_Varient, Items, Sales
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
#        fields = ['productname', 'product_description', 'status']
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Models
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class Feature_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureMaster
        fields = '__all__'


class Feature_VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature_Varient
        fields = '__all__'

class Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class Sales_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
