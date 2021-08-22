from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from users.serializers import LogoutSerializer


class LogoutViewSet(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = LogoutSerializer

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        responses={
            '200': "Logout User and blacklist tokens",
            '400': "Bad Request"
        },
        security=[],
        operation_id='LogoutUser',
        operation_description='Logout Users',
        tags=['Login/Logout'],
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.logout_user(request, serializer.validated_data['refresh']):
            return Response(data={'status': 'true', 'details': 'token in blacklist'},
                            status=status.HTTP_205_RESET_CONTENT)
