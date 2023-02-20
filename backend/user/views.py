from django.shortcuts import render
from backend.product.utils import SetProductPaginationResult
from rest_framework import mixins, generics
from rest_framework import status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .utils import emailBookingNotification
# Create your views here.

class BookingViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):

        data = request.data
        context = {}
        
        book, created = Booking.objects.get_or_create(
            first_name =data['first_name'],
            last_name= data['last_name'],
            phone_number = data['phone_number'],
            email= data['email'],
            choice=data['choice'],
            address=data['address'],
            city= data['city'],
            state = data['state'],
            country = data['country']
        )
        if not created:
            book.completed = False
            book.save()
            context['status'] = status.HTTP_200_OK
        else:
            context['status'] = status.HTTP_201_CREATED
        context['message'] = "process success"

        emailBookingNotification(request, book)

        return Response(context)
        #return self.create(request)