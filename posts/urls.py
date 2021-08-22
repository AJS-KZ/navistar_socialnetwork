from django.urls import path, re_path

from posts.views import PostViewSet, AnaliticViewSet


urlpatterns = [
    path('create/', PostViewSet.as_view({'post': 'create'})),
    path('', PostViewSet.as_view({'get': 'list'})),
    path('analitic/', AnaliticViewSet.as_view()),

    re_path(r'^like_dislike/(?P<pk>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$',
            PostViewSet.as_view({'put': 'add_like'})),
]
