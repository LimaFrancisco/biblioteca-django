from rest_framework import serializers
from .models import Book, Collection

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        user = self.context['request'].user
        return Collection.objects.create(user=user, **validated_data)
