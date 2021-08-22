from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from users.views import (
    LoginViewSet,
    LogoutViewSet,
    UserViewSet,
    UserLastActivityViewSet,
)


router = DefaultRouter()

router.register('', UserViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view()),
    path('logout/', LogoutViewSet.as_view()),
    path('last_activity/', UserLastActivityViewSet.as_view())
] + router.urls
