from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, private_key = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({'uuid': user.uuid, 'public_key': user.public_key, 'private_key': private_key},
                        status=status.HTTP_201_CREATED, headers=headers)
