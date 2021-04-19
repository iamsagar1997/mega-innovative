from rest_framework import serializers
from .models import Contact, Ourwork, Testomonial


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone', 'message')


class OurworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ourwork
        fields = ('id', 'title', 'desc', 'image', 'website', 'facebook', 'instagram')


class TestomonialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testomonial
        fields = ('id', 'title', 'message', 'image')