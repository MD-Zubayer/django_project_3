from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .forms import Post1Form
# Create your views here.
def home(request):
    context = {
        'title': 'My Portfolio',
    'projects': [
        {'name': 'Flower Bank', 'tech': 'JS, Tailwind'},
        {'name': 'To-Do App', 'tech': 'HTML, CSS'},
        {'name': 'Django Blog', 'tech': 'Python, Django'},
    ]
    }

    return render(request, 'home.html', context)
    # return HttpResponse('this is django app')

def profile(request):
    data = {
        'username': 'md junayed',
        'email': 'jonayed@444gmail.com', 
        'is_varified': False,

    }

    return render(request, 'profile.html', data)

def blog_post(request):
    data = {
        'title': 'My first blog post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at lorem at nulla bibendum...',
         'published_date': datetime(2025,8,1),

    }

    return render(request, 'blog.html', data)

def dashboard(request):
    data = {
        'is_logged_in': False,
        'username': 'junayed',
    }

    return render(request, 'dashboard.html', data)

def product_list(request):
    data = {
        'products': ['Laptop', 'Mouse', 'Keyboard', 'Mobaile']
    }

    return render(request, 'products.html', data)

def blog_list(request):
    
    posts = [
    {'title': 'Post 1', 'author': 'Zubayer'},
    {'title': 'Post 2', 'author': 'Jonayed'},
    {'title': 'Post 3', 'author': 'Tefheema'}
    ]

    return render(request, 'blog_list.html', {"posts":posts})

def form1(req):
    submitted = False
    submitted_name = ''

    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')

        print('Name:  ', name)
        print('Email :', email)

        submitted = True
        submitted_name = name
    
    return render(req, 'form1.html', {'submitted': submitted, 'submitted_name': submitted_name 
                                        
    })

def form2(req):
    submitted = False
    massege = ''
    
    if req.method == 'POST':
        number = req.POST.get('number')

        print('Phone Number :', number)

        submitted = True
        massege = 'Thanks for giving your number!'
    return render(req, 'form2.html', {'submitted': submitted, 'massege': massege})

def create_post1(req):
    if req.method == 'POST':
        form = Post1Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = Post1Form()
    return render(req, 'post1.html', {'form': form})