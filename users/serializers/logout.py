from rest_framework.serializers import Serializer, CharField
from rest_framework.validators import ValidationError
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(Serializer):
    refresh = CharField(max_length=1000, required=True)

    def validate(self, attrs):
        if 'refresh' not in attrs.keys():
            raise ValidationError('refresh token not found')

        return attrs

    def logout_user(self, request, refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return True
        except:
            raise ValidationError("it's refresh token not from our backend")
