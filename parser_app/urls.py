from django.urls import path
from . import views

urlpatterns = [
    path('start_parsing/', views.ParseFormNewsView.as_view(), name='parser'),
    path('news_parse_list/', views.ParseNewsListView.as_view(), name='news_list'),
]