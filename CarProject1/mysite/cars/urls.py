from tkinter.font import names

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'models', ModelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]