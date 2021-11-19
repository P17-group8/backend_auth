from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.facturas import Factura
from .models.plazas import Plazas
from.models.tarifa import Tarifa
from.models.usuarios import Usuarios
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Factura)
admin.site.register(Plazas)
admin.site.register(Tarifa)
admin.site.register(Usuarios)

# Register your models here.
