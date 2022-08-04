from django.contrib import admin
from django.urls import path
from . import views
from .views import FeedBackView, DoneView, FeedBackUpdateView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate

urlpatterns = [
    # Implementing logic with class-based way
    path('', FeedBackView.as_view()),
    path('done', DoneView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
    path('update/<int:pk>', FeedBackViewUpdate.as_view()),
]
