from django.contrib                 import admin
from django.urls                    import path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from app_operator                   import views 

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MS - Authentication - Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


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
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
