
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, default='No description added')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz')
    is_public = models.BooleanField()

    def __str__(self):
        return self.quiz_name
    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    quistion_text = models.TextField(null=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')

    def __str__(self):
        return self.id  
    def get_answers(self):
        return self.option_set.all()     

class Option(models.Model):
    option_text = models.TextField(null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    is_correct = models.TextField(default=False)

    def __str__(self):
        return self.id             




