from rest_framework import status, views
from rest_framework.response import Response
from parqueaderoapp.serializers.usuariosSerializer import UsuariosSerializer


class createUsuariosView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuariosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

