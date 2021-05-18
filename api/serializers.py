
from rest_framework import serializers
from .models import *

class ShoesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shoes
        fields = '__all__'

class ZayavkaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Zayavka
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ShoesListRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoes
        fields = '__all__'

class ShoesDetailSerializers(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Shoes
        fields = '__all__'

    @staticmethod
    def get_posts(obj):
        return ShoesSerializers(Shoes.objects.filter(blog_category=obj),many=True).data



class BlogCategoryDetailSerializers(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def get_posts(obj):
        return ShoesSerializers(Shoes.objects.filter(blog_category=obj),many=True).data