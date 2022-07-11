from django.urls import path
from .views import (NewsListView, 
NewsDetailView, 
NewsCreateView,
NewsUpdateView,
NewsDeleteView,)
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/new/', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete'),
    path('admission', views.admission, name='admission'),
    path('events', views.events, name='events'),
]
