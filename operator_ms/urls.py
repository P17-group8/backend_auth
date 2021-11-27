from django.contrib import admin
from django.urls import path
from app_operator import views 
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from app_operator.views import VerifyTokenView

urlpatterns = [
    path('admin/',             admin.site.urls),
    path('login/',             TokenObtainPairView.as_view()),
    path('refresh/',           TokenRefreshView.as_view()),
    path('verifyToken/',       VerifyTokenView.as_view(), name='token_verify'),
    path('operador/create/',   views.OperadorCreateView.as_view()),
    path('operador/<int:pk>/', views.OperadorDetailView.as_view()),
]
