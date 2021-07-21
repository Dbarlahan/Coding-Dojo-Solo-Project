from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
import json
import requests
from .models import User, Quiz

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_password = request.POST['password']
        hash_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            photo_url = request.POST['photo_url'],
            password = hash_password,
        )
        request.session['user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        request.session['email'] = new_user.email
        request.session['photo_url'] = new_user.photo_url
        return redirect('/home')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        logged_user = User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                request.session['first_name'] = logged_user.first_name
                request.session['last_name'] = logged_user.last_name
                request.session['email'] = logged_user.email
                request.session['photo_url'] = logged_user.photo_url
                return redirect('/home')
            else:
                messages.error(request, 'Invalid Email or Password')
        else:
            messages.error(request, 'Please enter valid Email and Password to Sign In')
    return redirect('/')

    
def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        quotes = 'https://zenquotes.io/api/random'
        response = requests.get(quotes).json()
        
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'quizzes': Quiz.objects.all().filter(user=user),
            'quotes': response[0]
        }
        return render(request, 'home.html', context)

def account(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'account.html', context)
        

def create_page(request):
    return render(request, 'create_page.html')
        
def create_quiz(request):
    if request.method == "POST":
        errors = Quiz.objects.quiz_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/create_page')
        else:
            new_quiz = Quiz.objects.create(
                title = request.POST['title'],
                description = request.POST['description'],
                question_1 = request.POST['question_1'],
                answer_1 = request.POST['answer_1'],
                question_2 = request.POST['question_2'],
                answer_2 = request.POST['answer_2'],
                question_3 = request.POST['question_3'],
                answer_3 = request.POST['answer_3'],
                question_4 = request.POST['question_4'],
                answer_4 = request.POST['answer_4'],
                question_5 = request.POST['question_5'],
                answer_5 = request.POST['answer_5'],
                user = User.objects.get(id=request.session['user_id'])
            )
            new_quiz.save()
            return redirect('/home')
    else:
        return redirect('/')

def view_quiz(request, quiz_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        one_quiz = Quiz.objects.get(id=quiz_id)
        context = {
            'quiz': one_quiz
        }
        return render(request, 'view_quiz.html', context)


def edit_page(request, quiz_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        one_quiz = Quiz.objects.get(id=quiz_id)
        context = {
            'quiz': one_quiz
        }
        return render(request, 'edit_page.html', context)


def edit_quiz(request, quiz_id):
    if request.method == "POST":
        errors = Quiz.objects.quiz_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect(f'/edit_page/{quiz_id}')
        else:
            to_update = Quiz.objects.get(id=quiz_id)
            to_update.title = request.POST['title']
            to_update.description = request.POST['description']
            to_update.question_1 = request.POST['question_1']
            to_update.answer_1 = request.POST['answer_1']
            to_update.question_2 = request.POST['question_2']
            to_update.answer_2 = request.POST['answer_2']
            to_update.question_3 = request.POST['question_3']
            to_update.answer_3 = request.POST['answer_3']
            to_update.question_4 = request.POST['question_4']
            to_update.answer_4 = request.POST['answer_4']
            to_update.question_5 = request.POST['question_5']
            to_update.answer_5 = request.POST['answer_5']
            to_update.save()
            messages.success(request, 'Quiz successfully updated')
            return redirect(f'/edit_page/{quiz_id}')
    
def delete(request, quiz_id):
    Quiz.objects.get(id=quiz_id).delete()
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')