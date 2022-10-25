from django.urls import path, include
from .views import *
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('genre/<str:slug>', get_genre, name='genre'),
    path('author/id<int:author_id>', get_author, name='author'),
    path('search/', search, name='search'),
    path('book/id<int:book_id>', get_book, name='book'),
    path('book/id<int:book_id>/leave_comment', leave_comment, name='leave_comment'),
]


