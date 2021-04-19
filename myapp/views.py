from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ContactSerializer, OurworkSerializer, TestomonialSerializer
from .models import Contact, Ourwork, Testomonial

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class OurworkViewSet(viewsets.ModelViewSet):
    queryset = Ourwork.objects.all()
    serializer_class = OurworkSerializer

class TestomonialViewSet(viewsets.ModelViewSet):
    queryset = Testomonial.objects.all()
    serializer_class = TestomonialSerializer
