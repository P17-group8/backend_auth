from rest_framework                                 import status, views
from rest_framework.response                        import Response
from rest_framework_simplejwt.serializers           import TokenObtainPairSerializer
#ELM - Creo que este era el error, al importar el serializer faltaba adicionar el .serializers.operadorSerializer 
from app_operator.serializers.operadorSerializer    import OperadorSerializer

class OperadorWelcomeView(views.APIView):
    def get(self, request, *args, **kwargs):
        message = {"Detail" : "Welcome to AuthMS-Operador."}
        return Response(message, status=status.HTTP_200_OK)


class OperadorCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
   #     print('a')
        serializer = OperadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        token_data = {'username':request.data['username'],
                      'password':request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)