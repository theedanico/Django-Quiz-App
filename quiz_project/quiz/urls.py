from django.urls import path
from .views import addQuestion,deleteQuestion, home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('question/', addQuestion, name='add_question'),
    path('delete_question/<int:quest_id>', deleteQuestion, name='delete_question')
]


