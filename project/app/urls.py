from django.urls import path
from .views import *

urlpatterns = [
    path('', AuthorCreateView.as_view(), name='add_author'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('add_borrowrecord/', BorrowRecordCreateView.as_view(), name='add_borrowrecord'),

    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('borrowrecords/', BorrowRecordListView.as_view(), name='borrowrecords_list'),
    
    path('Author_to_excel/',Author_to_excel, name='Author_to_excel'),
    path('Books_to_excel/',Books_to_excel, name='Books_to_excel'),
    path('Borrowrecords_to_excel/',Borrowrecords_to_excel, name='Borrowrecords_to_excel'),
]
