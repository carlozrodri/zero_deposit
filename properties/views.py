from rest_framework import viewsets, permissions
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied



class PropertyViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing Property instances. Only authenticated users 
    can access this viewset, and users can only view, update, or delete 
    properties that they created.

    Attributes:
        queryset: The base queryset to retrieve all Property objects.
        serializer_class: The serializer used for Property objects.
        permission_classes: Ensures that only authenticated users 
                            can access this viewset.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Overrides the default queryset to filter properties by the 
        currently authenticated user, showing only properties created 
        by them.
        
        Returns:
            Queryset of Property objects created by the current user.
        """

        return Property.objects.filter(created_by=self.request.user)
    def perform_create(self, serializer):
        """
        Custom create method to set the 'created_by' field to the 
        current user when a new property is created.

        Args:
            serializer: The serializer instance that will save the data.
        """
        serializer.save(created_by=self.request.user)
    def perform_update(self, serializer):
        """
        Custom update method to restrict updates to properties that 
        the current user has created. Raises a PermissionDenied 
        exception if the user attempts to update a property they 
        didn't create.

        Args:
            serializer: The serializer instance that will save the data.
        
        Raises:
            PermissionDenied: If the current user is not the creator of 
                              the property being updated.
        """
        if serializer.instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to update this property.")
        super().perform_update(serializer)
