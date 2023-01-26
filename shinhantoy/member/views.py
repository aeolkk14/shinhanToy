from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password, make_password

from .serializers import MemberSerializer
from .models import Member

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    serializer_class = MemberSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


    
class MemberChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *Args, **kwargs):
        current = request.data.get('current')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if password1 != password2:
            return Response({
                'detail': 'Wrong new password',
            }, status=status.HTTP_400_BAD_REQUEST)

        member = request.user
        if not check_password(current, member.password):
            return Response({
                'detail': 'Wrong new password',
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password1)
        member.save()

        return Response(status=status.HTTP_200_OK)