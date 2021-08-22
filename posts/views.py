from rest_framework import status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collections import Counter
from itertools import groupby
from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView

from posts.filters import DateRangeFilterSet
from posts.models import Post, PostLike
from posts.serializers import PostSerializer, PostLikeSerializer


class PostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'add_like' or self.action == 'add_dislike':
            serializer_class = PostLikeSerializer

        return serializer_class

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def add_like(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request,
                                                                     'kwargs': kwargs})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AnaliticViewSet(GenericAPIView):
    queryset = PostLike.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        ordered_queryset = filtered_queryset.order_by('date')
        likes_by_date = groupby(ordered_queryset, lambda like: like.date.strftime("%Y-%m-%d"))

        response = []
        for date, likes in likes_by_date:
            count = Counter(like.like for like in likes)
            response.append(
                {
                    'Date': date,
                    'Likes': count['LIKE'],
                    'Dislikes': count['DISLIKE'],

                }
            )

        return Response(data=response, status=status.HTTP_200_OK)
