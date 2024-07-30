from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts =  [
    { 
    'author' : 'Juan Moreno',
    'tittle': 'Blog Post1',
    'content':'este es mi prumer project de Full stack',
    'date_poster': "26 de Augost, 2022"
    },

    {
    'author' : 'Juan Pinbzon',
    'tittle': 'Blog Post2',
    'content' : 'este es mi primer projecto con code institud',
    'date_poster': '30 de Augost, 2021'

    }
]
  
  
def home(request):
    context = {
        'posts': posts
    }
    return render(request,"blog/home.html", context)

def about(request):
    return render(request,"blog/about.html")

    