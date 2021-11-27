from rest_framework import status, views
from rest_framework.response import Response
from app_operator.serializers import OperadorSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class OperadorCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = OperadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        token_data = {'username':request.data['username'],
                      'password':request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)