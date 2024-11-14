
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from properties.models import Property
from rest_framework.test import APIClient


class PropertyViewSetTestCase(TestCase):
    
    def setUp(self):
        # Set up test data and environment
        # Create a regular user and an admin user for testing
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.admin_user = User.objects.create_user(username="adminuser", password="adminpass123", is_admin=True)

        # Initialize API client for making requests
        self.client = APIClient()

    def authenticate(self, user):
        # Helper method to authenticate a user by obtaining and setting a JWT token
        password = "testpass123" if user == self.user else "adminpass123"
        response = self.client.post(reverse("token_obtain_pair"), {"username": user.username, "password": password})
        
        # Ensure token retrieval was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Set the JWT token for authenticated requests
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    def test_property_creation_with_authenticated_user(self):
        # Verify that an authenticated user can create a new property
        self.authenticate(self.user)

        property_data = {
            "address": "123 Test Street",
            "postcode": "T12345",
            "city": "Testville",
            "rooms": 3,
        }

        # Send the request to create a property
        response = self.client.post(reverse("property-list"), property_data)
        
        # Check that the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the property was actually created in the database
        created_property = Property.objects.get(address="123 Test Street")
        self.assertEqual(created_property.created_by, self.user)

    def test_property_creation_with_unauthenticated_user(self):
        # Verify that a property cannot be created without authentication
        unauth_property_data = {
            "address": "456 Unauth Street",
            "postcode": "U12345",
            "city": "Unauthorized",
            "rooms": 2,
        }

        # Attempt to create a property without authenticating
        response = self.client.post(reverse("property-list"), unauth_property_data)
        
        # Ensure the request was denied due to lack of authentication
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_property_list_with_authenticated_user(self):
        # Verify that an authenticated user can retrieve a list of their properties
        self.authenticate(self.user)
        
        # Create a test property associated with the authenticated user
        Property.objects.create(address="123 Test Street", postcode="T12345", city="Testville", rooms=3, created_by=self.user)

        # Request the list of properties
        response = self.client.get(reverse("property-list"))
        
        # Verify the response status and contents
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["address"], "123 Test Street")
