from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class ExampleUserView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        content = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(content)
