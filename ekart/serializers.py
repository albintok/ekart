from ekart.models import Catagories,Products
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Catagories
        fields=["catagory_name","is_active","id"]


class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    catagory=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"
    def create(self, validated_data):
        catagory=self.context.get("category")
        return Products.objects.create(**validated_data,catagory=catagory)

