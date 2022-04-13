from django.urls import path
from .views import addQuestion,deleteQuestion, home, profile, RegisterView, addQuiz, exploreQuiz,  myquizzes

urlpatterns = [
    path('', home, name='users-home'),
    
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('question/<int:quiz_id>', addQuestion, name='add_question'),
    path('delete_question/<int:quiz_id>/<int:quest_id>', deleteQuestion, name='delete_question'),
    # path('edit_question/<int:quiz_id>/<int:quest_id>', editQuestion, name='edit_question'),
    path('question/', addQuestion, name='add_question'),
    path('delete_question/<int:quest_id>', deleteQuestion, name='delete_question'),
    path('add_quiz/',addQuiz, name='add_quiz' ),
    path('explore_quizzes/', exploreQuiz, name="explore_quizzes"),
    path('myquizzes/', myquizzes, name='myquizzes')
]


