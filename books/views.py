from django.shortcuts import render
from .models import Book
from django.http import Http404

# Create your views here.
def index(request):
    newest_books = Book.objects.order_by('-release_date')[:15]
    context = {'newest_books': newest_books}
    return render(request, 'books/index.html', context)
    
    
def show(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/show.html', {'book': book})