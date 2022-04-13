from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Question,Option,Quiz,QuestionOptions
import json
from .forms import QuizForm, QuestionForm
from django.http import JsonResponse
from django.contrib.auth.models import User


from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm       

def home(request):
    return render(request, 'quiz/index.html')

def takeQuiz(request,quiz_id):
    quiz     =  Quiz.objects.filter(id = quiz_id).first() 
    questions =  Question.objects.filter(quiz_id = quiz_id).all() 
    quiz_content = []
    for quest in questions :
       q  = QuestionOptions()
       q.mQuestion = quest
       q.options = Option.objects.filter(question = quest.id).all() 
       quiz_content.append(q)
    
    return render(request, 'quiz/take_quiz.html',{"quiz_content":quiz_content,"quiz":quiz})

def exploreQuiz(request):
    quiz = Quiz.objects.all()
    quiz_set = {'quiz': quiz}
    return render(request, 'quiz/quizlist.html', quiz_set)

def deleteQuestion(request,quiz_id,quest_id):
    if quest_id:
       Question.objects.filter(id = quest_id).delete() 
    return redirect(f"../../question/{quiz_id}")

def editQuestion(request,quiz_id,quest_id):
    questions =  Question.objects.filter(quiz_id = quiz_id).all
    if request.method == "POST":
        quistionText = request.POST.get('quistion_text')
        option_text = request.POST.get('option_text')
        options = request.POST.get('options')
        if not quistionText or not option_text:
                messages.error(request, "Please add question text")
                messages.error(request, "Please add default option")  
        else:        
                options = json.loads(options)
                mQuestion = Question.objects.first()
                mQuestion.quistion_text = quistionText
                mQuestion.quiz = Quiz.objects.filter(id = quiz_id).first()
                mQuestion.save()

                for option in options :
                    mOption =Option()
                    mOption.option_text = option
                    mOption.question = mQuestion
                    if option_text==option:
                        mOption.is_correct = True
                    mOption.save()  
                    messages.success(request, "Question updated successfully")
        return redirect(f"../../question/{quiz_id}")
    
    if quest_id:
       selectedQuestion =  Question.objects.filter(id = quest_id).first() 
       options = Option.objects.filter(quest_id = quest_id).all()
    return render(request, 'quiz/add_question.html',{"itemsQuestions": questions,"selectedQuestion":selectedQuestion,"quiz_id":quiz_id,"options":options})        

def addQuestion(request,quiz_id):
    if request.method == "POST":
        quistionText = request.POST.get('quistion_text')
        option_text = request.POST.get('option_text')
        options = request.POST.get('options')
        if not quistionText or not option_text:
                messages.error(request, "Please add question text")
                messages.error(request, "Please add default option")  
        else:        
                options = json.loads(options)
                mQuestion = Question()
                mQuestion.quistion_text = quistionText
                mQuestion.quiz = Quiz.objects.filter(id = quiz_id).first()
                mQuestion.save()

                for option in options :
                    mOption =Option()
                    mOption.option_text = option
                    mOption.question = mQuestion
                    if option_text==option:
                        mOption.is_correct = True
                    mOption.save()  
                    messages.success(request, "Question added successfully")

    
    questions =  Question.objects.filter(quiz_id = quiz_id).all
    return render(request, 'quiz/add_question.html',{"itemsQuestions": questions,"quiz_id":quiz_id})    
  
@login_required
def addQuiz(request):
    if request.method=="POST":
        form = QuizForm(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            messages.success(request, 'Your Quizz has been created successfully')
            return redirect(to = 'myquizzes' )
    else:
        form=QuizForm()
    
    return render(request, "quiz/add_quiz.html", {'form':form})
@login_required
def myquizzes(request, pk=None):
    if pk:
        quiz_owner = get_object_or_404(User, pk=pk)
        user_quizzes = Quiz.objects.filter(author=request.user)
    else:
        quiz_owner = request.user
        user_quizzes = Quiz.objects.filter(author=request.user)
        
    return render(request, 'quiz/myquizzes.html', {'quiz_owner': quiz_owner, 'user_quizzes': user_quizzes})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'quiz/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'quiz/password_reset.html'
    email_template_name = 'quiz/password_reset_email.html'
    subject_template_name = 'quiz/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'quiz/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'quiz/profile.html', {'user_form': user_form, 'profile_form': profile_form})




