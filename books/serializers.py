from django.contrib.auth.models import User
from books.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'slug', 'text', 'posted_date','autor', 'price', 'quantity')

class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opinion
        fields = ('url', 'id', 'book_id', 'opinion')