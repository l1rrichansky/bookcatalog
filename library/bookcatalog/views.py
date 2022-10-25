from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from .models import *


def index(request):
    books = Book.objects.all().order_by('-id')
    page_objects = get_paginator(books, request)
    context = {
        'books': books,
        'page_obj': page_objects
    }
    return render(request, 'bookcatalog/index.html', context)


def get_genre(request, slug):
    genre = Genre.objects.get(slug=slug)
    books = Book.objects.filter(genres__slug=slug).order_by('-id')
    page_objects = get_paginator(books, request)
    context = {
        'books': books,
        'genre': genre,
        'page_obj': page_objects
    }
    return render(request, 'bookcatalog/genre.html', context)


def get_author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author).order_by('-id')
    page_objects = get_paginator(books, request)
    context = {
        'books': books,
        'author': author,
        'page_obj': page_objects
    }
    return render(request, 'bookcatalog/author.html', context)


def search(request):
    books = Book.objects.filter(Q(title__icontains=request.GET.get('s')) | Q(author__name__icontains=request.GET.get('s')))
    page_objects = get_paginator(books, request)
    context = {
        'books': books,
        'search_phrase': request.GET.get('s'),
        'search_str': f"s={request.GET.get('s')}&",
        'page_obj': page_objects
    }
    return render(request, 'bookcatalog/search.html', context)


def get_book(request, book_id):
    book = Book.objects.get(id=book_id)
    comments = Comment.objects.filter(book=book).order_by('-id')
    context = {
        'book': book,
        'comments' : comments,
    }
    return render(request, 'bookcatalog/book_view.html', context)


def leave_comment(request, book_id):
    book = Book.objects.get(id=book_id)
    book.comment_set.create(author_name=request.POST.get('name'), comment_text=request.POST.get('text'), author_email=request.POST.get('email'))
    return HttpResponseRedirect(reverse('book', args = (book.id,)))


def get_paginator(objects, request, k=6):
    paginator = Paginator(objects, k)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return page_objects
