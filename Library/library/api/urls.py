from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/create', UserCreateView.as_view()), # post method for user
    path('user/list', UserListView.as_view()), # get method for list of users
    path('user/detail/<int:pk>/', UserDetailView.as_view()), # get,put,delete methods for user by id
    path('user/<user_id>/order/', UserOrdersListView.as_view()), # get,put,delete methods for orders by user id
    path('author/create', AuthorCreateView.as_view()), # post method for author
    path('author/list', AuthorListView.as_view()), # get method for list of authors
    path('author/detail/<int:pk>/', AuthorDetailView.as_view()), # get,put,delete methods for author by id 
    path('book/create', BookCreateView.as_view()), # post method for book
    path('book/list', BookListView.as_view()), # get method for list of books
    path('book/detail/<int:pk>/', BookDetailView.as_view()), # get,put,delete methods for book by id
    path('order/create', OrderCreateView.as_view()), # post method for order
    path('order/list', OrderListView.as_view()), # get method for list of orders
    path('order/detail/<int:pk>/', OrderDetailView.as_view()), # get,put,delete methods for order by id
    ]