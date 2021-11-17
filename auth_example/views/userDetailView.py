from rest_framework                              import generics

from auth_example.models.user                    import User
from auth_example.serializers.userSerializer     import UserSerializer


class UserDetailView(generics.RetrieveAPIView):#CUando es un dato es RetrieveAPIView, cuando son varios es ListAPIView #Mirar el Live
    queryset           = User.objects.all()#trae todos los datos sin filtrar
    serializer_class   = UserSerializer
    def get(self, request, *args, **kwargs): #Token BEARER_TOKEN (empieza en el caracter 7)
        return super().get(request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):#CUando es un dato es RetrieveAPIView, cuando son varios es ListAPIView #Mirar el Live
    queryset           = User.objects.all()#trae todos los datos sin filtrar
    serializer_class   = UserSerializer
    def update(self, request, *args, **kwargs): #Token BEARER_TOKEN (empieza en el caracter 7)
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):#CUando es un dato es RetrieveAPIView, cuando son varios es ListAPIView #Mirar el Live
    queryset           = User.objects.all()#trae todos los datos sin filtrar
    serializer_class   = UserSerializer
    def update(self, request, *args, **kwargs): #Token BEARER_TOKEN (empieza en el caracter 7)
        return super().destroy(request, *args, **kwargs)