from django.shortcuts import Http404
from rest_framework import mixins, viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from users.permissions import UserPermission
from users.serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserLastActivitySerializer
)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission, ]

    def get_serializer_class(self):
        serializer_class = UserSerializer

        if self.action == 'create':
            serializer_class = UserCreateSerializer
        elif self.action == 'update':
            serializer_class = UserUpdateSerializer
        return serializer_class

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(uuid=kwargs['pk'])
            serializer = self.get_serializer(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            raise Http404

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = self.serializer_class().data
        refresh = RefreshToken.for_user(user)
        response['tokens'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data=response, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        try:
            instance = self.queryset.get(uuid=kwargs['pk'])
        except:
            raise Http404

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserLastActivityViewSet(views.APIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLastActivitySerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
