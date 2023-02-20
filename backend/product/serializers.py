from rest_framework import serializers
from .models import Product, Category
import json

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField()
    product_category =serializers.SerializerMethodField()

    #####################################################
    ## product category for serializing manytomany data #
    #####################################################
    def get_product_category(self, obj):
        category = obj.product_category
        data = category.category_name
        return data


    #####################################################
    ## product category for serializing manytomany data #
    #####################################################
    """
    def get_product_category(self, obj):
        category_list=[]
        for item in obj.product_category.all():
            category_list.append(item.category_name)
        return category_list
    """
        

    def get_absolute_url(self, obj):
        request_self = self.context.get('request')
        host_name = request_self.get_host()
        protocol = request_self.scheme
        url = obj.get_absolute_url()
        #print(host_name, protocol, url)
        built_url = f"{protocol}://{host_name}{url}"
        return built_url


    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_category', 'product_image', 'description', 'slug', "absolute_url"]