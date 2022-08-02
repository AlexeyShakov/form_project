from django.contrib import admin
from django.urls import path
from . import views
from .views import FeedBackView

urlpatterns = [
    # Implementing logic with class-based way
    path('', FeedBackView.as_view()),
    path('done', views.done),
    path('<int:id_feedback>', views.update_feedback),

]
