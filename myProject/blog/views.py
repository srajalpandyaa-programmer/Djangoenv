from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
'''
def home(request):
    return HttpResponse('<h1>Welcome to my blog</h1>')

def about(request):
    return HttpResponse("Blog's about page")

def post_details(request,post_id):
    return HttpResponse(f"<h1>Details of blog post {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Profile of User:{username}</h1>")


def article_by_year(request,year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")

def article_by_date(request,**kwargs):
    return HttpResponse(f'<h1>Data: {kwargs} </h1>')


def post_list(request):
    return render(request, 'blog/post_list.html')

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name":"Srajal Pandya",
        "age": 25,
        "skill":["python","django","fastapi"],
        "user":User("Pandya",27),
        "blog":{
            "title": "Django Template Introduction",
            "content": "<b>This is Django</b>",
            "created_at": datetime(2026,9,26,16,10)
        },
        "empty_value": None,
    }
    return render(request,"blog/home.html",context)


def blog_details(request):
    post ={
        "title":"My Second Template Post",
        "descriptions": "Django is a high level python framework.",
        "author":None,
        "created_at": datetime(2026,9,26,17,3),
        "comment_count": 3,
        "tags": ["python","django","fastapi"],
        "price":100,
        "number": 7,


    }
    return render(request,"blog/blog_details.html",{"post":post})

def blog_list(request):
    blogs = [
        {"title":"Django Basics","is_featured":True,"author":"Srajal Pandya"},
        {"title":"Django Advanced","is_featured":False,"author":""},
        {"title":"Django Rest Framework","is_featured":False,"author":"Jack Sparrow"}
    ]
    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code":"<h1>Welcome To My Blog</h1>",
    }
    return render(request, 'blog/blog_list.html', context)



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'blog/about.html')
'''

def home(request):
    return render(request, 'index.html')

def blog(request):
    students_list =[
        {"name":"Srajal","class":"10th"},
        {"name":"Mohit","class":"9th"},
        {"name":"Kratik","class":"8th"},
    ]
    return render(request,'blog/blog.html', {'students': students_list})