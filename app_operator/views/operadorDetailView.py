from rest_framework                              import generics, status
from rest_framework.response                     import Response
from app_operator.models.operador                import Operador
from app_operator.serializers.operadorSerializer import OperadorSerializer

class OperadorDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset           = Operador.objects.all()
    serializer_class   = OperadorSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)