from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from app_operator                   import views 

urlpatterns = [
        path('',                          views.OperadorWelcomeView.as_view()),
        path('admin/',                    admin.site.urls),
        path('login/',                    TokenObtainPairView.as_view()),
        path('refresh/',                  TokenRefreshView.as_view()),
        path('verifyToken/',              views.VerifyTokenView.as_view()),
        path('operador/',                 views.OperadorCreateView.as_view()),
        path('operador/<int:pk>/',        views.OperadorDetailView.as_view()),
        path('operador/update/<int:pk>/', views.OperadorUpdateView.as_view()),
        path('operador/delete/<int:pk>/', views.OperadorDeleteView.as_view()),
]
