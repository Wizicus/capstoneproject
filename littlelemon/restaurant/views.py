from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.bookingSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        items = models.Booking.objects.all()
        serializer = serializers.bookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON

    
class MenuItemView(ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.menuSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return [permission() for permission in permission_classes]
    

class SingleMenuItemView(RetrieveAPIView, DestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.menuSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return [permission() for permission in permission_classes]

  
def index(request):
    return render(request, 'index.html', {})