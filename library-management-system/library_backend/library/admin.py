from django.contrib import admin
from .models import Book, BorrowTransaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'copies_available')
    search_fields = ('title', 'author', 'isbn')

@admin.register(BorrowTransaction)
class BorrowTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'borrow_date', 'return_date')
    list_filter = ('status', 'borrow_date')
    search_fields = ('user__username', 'book__title')
