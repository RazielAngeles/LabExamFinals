from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, BorrowTransaction
from .serializers import BookSerializer, BorrowTransactionSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
def borrow_book(request):
    user_id = request.data['user']
    book_id = request.data['book']
    book = Book.objects.get(id=book_id)

    if book.copies_available <= 0:
        return Response({'error': 'No copies available'}, status=400)

    book.copies_available -= 1
    book.save()

    transaction = BorrowTransaction.objects.create(
        user_id=user_id,
        book_id=book_id,
        status='borrowed'
    )
    return Response(BorrowTransactionSerializer(transaction).data)

@api_view(['POST'])
def return_book(request, borrow_id):
    transaction = BorrowTransaction.objects.get(id=borrow_id)
    transaction.status = 'returned'
    transaction.return_date = request.data.get('return_date')
    transaction.save()

    book = transaction.book
    book.copies_available += 1
    book.save()

    return Response(BorrowTransactionSerializer(transaction).data)

@api_view(['GET'])
def all_transactions(request):
    transactions = BorrowTransaction.objects.all()
    serializer = BorrowTransactionSerializer(transactions, many=True)
    return Response(serializer.data)
