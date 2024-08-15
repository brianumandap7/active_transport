from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource, bikelanetbl
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class ATDBView(TemplateView):
    template_name = 'atdb/atdb.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # Add any additional context if needed
        })
        return context

class TowTblView(ListView):
    model = Typeofwork
    template_name = 'atdb/towtbl.html'
    context_object_name = 'tow'

class RTView(ListView):
    model = Region
    template_name = 'atdb/rt.html'
    context_object_name = 'rt'

class ATView(ListView):
    model = BikeArea
    template_name = 'atdb/at.html'
    context_object_name = 'at'

class RSView(ListView):
    model = RoadSection
    template_name = 'atdb/rs.html'
    context_object_name = 'rs'

class CLView(ListView):
    model = BikeClass
    template_name = 'atdb/cl.html'
    context_object_name = 'cl'

class FSView(ListView):
    model = FundSource
    template_name = 'atdb/fs.html'
    context_object_name = 'fs'

class MView(ListView):
    model = bikelanetbl
    template_name = 'atdb/maindb.html'
    context_object_name = 'maindb'

class towDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(Typeofwork.objects.values())
        return Response(prog)

class regDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(Region.objects.values())
        return Response(prog)

class areDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(BikeArea.objects.values())
        return Response(prog)

class roaDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(RoadSection.objects.values())
        return Response(prog)

class claDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(BikeClass.objects.values())
        return Response(prog)

class funDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(FundSource.objects.values())
        return Response(prog)

class bikDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(bikelanetbl.objects.values())
        return Response(prog)