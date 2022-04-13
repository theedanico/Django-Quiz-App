from django.urls import path
from .views import addQuestion,deleteQuestion,editQuestion ,home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('question/<int:quiz_id>', addQuestion, name='add_question'),
    path('delete_question/<int:quiz_id>/<int:quest_id>', deleteQuestion, name='delete_question'),
    path('edit_question/<int:quiz_id>/<int:quest_id>', editQuestion, name='edit_question')
]


