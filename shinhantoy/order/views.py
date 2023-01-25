from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .paginations import OrderLargePagination
from .serializers import OrderSerializer

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        return Order.objects.order_by('-id')
       

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)