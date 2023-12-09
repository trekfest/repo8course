from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking, MenuItem
from .serializers import MenuItemSerializer, MenuSerializer, BookingSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  

@api_view(['GET'])  # Specify the HTTP method for the view
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

# @api_view(['GET', 'POST'])  # Allow both GET and POST requests
# @permission_classes([AllowAny])  # Allow any user, authenticated or not, to access this view
# def obtain_auth_token_custom(request):
#     # Use the ObtainAuthToken view to handle token authentication
#     return ObtainAuthToken().post(request)