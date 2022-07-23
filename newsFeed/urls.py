from django.contrib import admin
from django.urls import path, include
from newsFeed import views
from .views import PostListView

app_name='newsFeed'

urlpatterns = [
    path('', PostListView.as_view(), name='viewNewsFeed'),
]
