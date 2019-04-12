from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductSerializer, BrandSerializer, CategorySerializer,ModelSerializer,VariantSerializer,Feature_masterSerializer, \
    Feature_VariantSerializer,Item_Serializer, Sales_Serializer
from .models import Product, Brand,ProductCategory,Product_Models,Variant,FeatureMaster,Feature_Varient, Items,Sales


class mymodelviewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

class brandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'id'

class categoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_field = 'id'

class modelViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    queryset = Product_Models.objects.all()
    lookup_field = 'id'

class variantViewSet(viewsets.ModelViewSet):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    lookup_field = 'id'

class FeatureMasterViewSet(viewsets.ModelViewSet):
    serializer_class = Feature_masterSerializer
    queryset = FeatureMaster.objects.all()
    lookup_field = 'id'

class FeatureVariantViewSet(viewsets.ModelViewSet):
    serializer_class = Feature_VariantSerializer
    queryset = Feature_Varient.objects.all()
    lookup_field = 'id'

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = Item_Serializer
    queryset = Items.objects.all()
    lookup_field = 'id'

class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = Sales_Serializer
    queryset = Sales.objects.all()
    lookup_field = 'id'

