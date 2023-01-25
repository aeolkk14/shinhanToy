from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'ord_no', 'ord_ymd')
        extra_kwargs = {
            'id':{
                'read_only': True
            }
        }
        