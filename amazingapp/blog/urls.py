from django.urls import path

from .views import BlogDetail, BlogList, BlogCreate, BlogEdit

app_name = 'blog'

urlpatterns = [
    path('<pk>/', BlogDetail.as_view(), name='detail'),
    path('', BlogList.as_view(), name='list'),
    path('new', BlogCreate.as_view(), name='new'),
    path('<pk>/', BlogEdit.as_view(), name='edit'),
]
