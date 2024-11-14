# views.py
from rest_framework import viewsets, permissions
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Property.objects.filter(created_by=self.request.user)
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    def perform_update(self, serializer):
        # Ensure the user can only update properties they've created
        if serializer.instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to update this property.")
        super().perform_update(serializer)
