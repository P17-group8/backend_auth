from django.contrib import admin
from django.urls import path
from app_operator import views 
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('operador/create/',views.OperadorCreateView.as_view()),
    path('operador/<int:pk>/',views.OperadorDetailView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
