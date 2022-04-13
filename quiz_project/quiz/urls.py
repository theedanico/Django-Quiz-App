from django.urls import path
<<<<<<< HEAD
from .views import addQuestion,deleteQuestion,editQuestion ,home, profile, RegisterView
=======
from .views import addQuestion,deleteQuestion, home, profile, RegisterView, addQuiz, exploreQuiz,  myquizzes
>>>>>>> 947d4ef2caf804fc7259508278c8f6233d7fce8c

urlpatterns = [
    path('', home, name='users-home'),
    
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('question/<int:quiz_id>', addQuestion, name='add_question'),
    path('delete_question/<int:quiz_id>/<int:quest_id>', deleteQuestion, name='delete_question'),
    path('edit_question/<int:quiz_id>/<int:quest_id>', editQuestion, name='edit_question'),
    path('question/', addQuestion, name='add_question'),
    path('delete_question/<int:quest_id>', deleteQuestion, name='delete_question'),
    path('add_quiz/',addQuiz, name='add_quiz' ),
    path('explore_quizzes/', exploreQuiz, name="explore_quizzes"),
    path('myquizzes/', myquizzes, name='myquizzes')
]


