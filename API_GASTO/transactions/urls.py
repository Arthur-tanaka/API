from django.urls import path
from rest_framework import routers
from .views import TransactionViewSet, saldo

router = routers.DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('saldo/', saldo)
] + router.urls
