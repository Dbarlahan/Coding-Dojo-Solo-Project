from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if postData['first_name'] == '':
            errors['first_name'] = 'First name cannot be empty'

        if postData['last_name'] == '':
            errors['last_name'] = 'Last name cannot be empty'

        if postData['email'] == '':
            errors['email'] = 'Email cannot be empty'
            
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
            
        if postData['photo_url'] == '':
            errors['photo_url'] = 'Photo Url cannot be empty'

        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = 'Email must be a valid format'

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and Confirm password doesn't match!"
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuizManager(models.Manager):
    def quiz_validator(self, postData):
        errors = {}
        
        if postData['title'] == '':
            errors['title'] = 'Title cannot be empty'

        if postData['description'] == '':
            errors['description'] = 'Description cannot be empty'
        
        if postData['question_1'] == '' or postData['question_1'] == '':
            errors['question_1'] = 'Question #1 cannot be empty'

        if postData['answer_1'] == '':
            errors['answer_1'] = 'Answer for Question #1 cannot be empty'
            
        if postData['question_2'] == '' or postData['question_2'] == '':
            errors['question_2'] = 'Question #2 cannot be empty'

        if postData['answer_2'] == '':
            errors['answer_2'] = 'Answer for Question #2 cannot be empty'
            
        if postData['question_3'] == '' or postData['question_3'] == '':
            errors['question_3'] = 'Question #3 cannot be empty'

        if postData['answer_3'] == '':
            errors['answer_3'] = 'Answer for Question #3 cannot be empty'
            
        if postData['question_4'] == '' or postData['question_4'] == '':
            errors['question_4'] = 'Question #4 cannot be empty'

        if postData['answer_4'] == '':
            errors['answer_4'] = 'Answer for Question #4 cannot be empty'
            
        if postData['question_5'] == '' or postData['question_5'] == '':
            errors['question_5'] = 'Question #5 cannot be empty'

        if postData['answer_5'] == '':
            errors['answer_5'] = 'Answer for Question #5 cannot be empty'
        
        return errors

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    question_1 = models.TextField()
    answer_1 = models.TextField()
    question_2 = models.TextField()
    answer_2 = models.TextField()
    question_3 = models.TextField()
    answer_3 = models.TextField()
    question_4 = models.TextField()
    answer_4 = models.TextField()
    question_5 = models.TextField()
    answer_5 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="user_quizzes", on_delete = models.CASCADE)
    objects = QuizManager()