from django.conf                                 import settings
from rest_framework                              import generics, status
from rest_framework.response                     import Response
from rest_framework.permissions                  import IsAuthenticated
from rest_framework_simplejwt.backends           import TokenBackend

from auth_example.models.user                    import User
from auth_example.serializers.userSerializer     import UserSerializer

class UserDetailView(generics.RetrieveAPIView):#CUando es un dato es RetrieveAPIView, cuando son varios es ListAPIView #Mirar el Live
    queryset           = User.objects.all()#trae todos los datos sin filtrar
    serializer_class   = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs): #Token BEARER_TOKEN (empieza en el caracter 7)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHN'])
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id']!= kwargs['pk']:
            stringResponse = {'detail': 'Acceso no autorizado'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)        
        return super().get(request, *args, **kwargs)