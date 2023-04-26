from django.shortcuts import render
from rest_framework import viewsets
from .models import Cours
from .serializer import CoursSerializer
from rest_framework.response import Response
# Create your views here.

class Cours_api(viewsets.ViewSet):
    
    def list(self, request):
        liste_cours = Cours.objects.all().order_by('date_publication')
        serialiazer = CoursSerializer(liste_cours, many=True).data
        return Response(serialiazer)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass