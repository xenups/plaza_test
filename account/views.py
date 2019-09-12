from rest_framework import parsers, decorators
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from .models import Profile
from .serializers import ProfilePicSerializer
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=ProfilePicSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)
