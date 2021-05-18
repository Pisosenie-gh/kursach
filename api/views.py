from django.shortcuts import render

from rest_framework import viewsets
# Create your views here.
from .models import *
from .serializers import *


class BlogCategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    action_to_serializer = {
        "retrieve": BlogCategoryDetailSerializers
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class ZayavkaViewSet(viewsets.ModelViewSet):

    queryset = Zayavka.objects.all()
    serializer_class = ZayavkaSerializers

    action_to_serializer = {
        "retrieve": ZayavkaSerializers
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    action_to_serializer = {
        "list": ShoesListRetriveSerializer,
        "retrieve": ShoesListRetriveSerializer,
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
