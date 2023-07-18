from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib  import auth
from django.shortcuts import redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet(request):
    form = SnippetForm()
    if request.method == 'POST':
        form = SnippetForm(request.POST or None)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect('snippets-list')

    return render(request, 'pages/add_snippet.html', {"form": form, "pagename": "Create Snippet"})


def snippets_page(request):
    snippets = Snippet.objects.all()
    return render(request, 'pages/view_snippets.html', {"snippets": snippets, "pagename": "List Snippets"})


def snippet(request, id):
    snippet = Snippet.objects.get(pk=id)
    return render(request, 'pages/snippet.html', {"item": snippet, "pagename": "View Snippet"})


def test(request):
    return render(request, 'demo_bootstrap.html')


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    if request.method == 'POST':
        snippet.delete()
    return redirect('snippets-list')


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    return render(request, 'pages/snippet.html', {"item": snippet, "pagename": "View Snippets"})

def snippet_edit(request, snippet_id):
    form = SnippetForm(request.POST or None)
    snippet = Snippet.objects.get(pk=snippet_id)
    return render(request, 'pages/snippet_edit.html', {"form": form, "pagename": "edit snippet"})

def login(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       print("username =", username)
       print("password =", password)

       return render(request,'pages/snippet_edit.html')

def login(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       # print("username =", username)
       # print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           pass
   return redirect('home')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')