from rest_framework                                 import generics#, status

from app_operator.models.operador                   import Operador
from app_operator.serializers.operadorSerializer    import OperadorSerializer
#

class OperadorDetailView(generics.RetrieveAPIView):
    queryset           = Operador.objects.all()
    serializer_class   = OperadorSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OperadorUpdateView(generics.UpdateAPIView):
    queryset           = Operador.objects.all()
    serializer_class   = OperadorSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class OperadorDeleteView(generics.DestroyAPIView):
    queryset           = Operador.objects.all()
    serializer_class   = OperadorSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)