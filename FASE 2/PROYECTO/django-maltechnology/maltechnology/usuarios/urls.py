from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserListView, InfoHornoListView, InfoProduccionListView

urlpatterns = [
    path('usuarios/', UserListView.as_view(), name='user-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info-horno/', InfoHornoListView.as_view(), name='info-horno-list'),
    path('info-produccion/', InfoProduccionListView.as_view(), name='info-produccion-list'),

]
