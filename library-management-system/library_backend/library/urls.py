from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, borrow_book, return_book, all_transactions

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/borrow/', borrow_book),
    path('api/return/<int:borrow_id>/', return_book),
    path('api/transactions/', all_transactions),
]
