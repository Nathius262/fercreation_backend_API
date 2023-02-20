from django.urls import path
from .views import BookingViewSet

app_name = 'user'

urlpatterns = [
    path('booking/', BookingViewSet.as_view()),
]