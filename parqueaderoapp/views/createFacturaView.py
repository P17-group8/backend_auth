from re import I
from rest_framework import status, views
from rest_framework.response import Response
from parqueaderoapp.serializers.facturaSerializer import FacturaSerializer


class createFacturaView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
