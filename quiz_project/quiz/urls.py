from django.urls import path
from .views import addQuestion, home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('question/', addQuestion, name='add-question')
]


