from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect, render
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


@login_required
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


@login_required
def snippets_page(request):
    snippets = Snippet.objects.all()
    return render(request, 'pages/view_snippets.html', {"snippets": snippets, "pagename": "List Snippets"})


def snippet(request, id):
    snippet = Snippet.objects.get(pk=id)
    return render(request, 'pages/snippet.html', {"item": snippet, "pagename": "View Snippet"})


def test(request):
    return render(request, 'demo_bootstrap.html')


@login_required
def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    if request.method == 'POST':
        snippet.delete()
    return redirect('snippets-list')


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    comments = snippet.comments.all()
    return render(request, 'pages/snippet.html', {"item": snippet, "comments": comments, "pagename": "View Snippets"})


def snippet_edit(request, snippet_id):
    form = SnippetForm(request.POST or None)
    snippet = Snippet.objects.get(pk=snippet_id)
    return render(request, 'pages/snippet_edit.html', {"form": form, "pagename": "edit snippet"})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
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


def registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.data.get('password1'))
            user.save()
            return redirect('home')

    return render(request, 'pages/registration.html', {"form": form, "pagename": "регистрация"})


@login_required
def snippet_my(request):
    my_snippet = Snippet.objects.filter(user=request.user)

    return render(request, 'pages/view_snippets.html', {'snippets': my_snippet})


@login_required
def comment_add(request, pk):
    if request.method == "GET":
        form = CommentForm()
        snippet = Snippet.objects.get(pk=pk)

        return render(request, 'pages/add_comment.html', {"form": form, "snippet": snippet })

    elif request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            snippet_id = request.POST.get("snippet_id")
            snippet = Snippet.objects.get(id=snippet_id)
            if snippet.id:
                comment = form.save(commit=False)
                comment.author = request.user
                comment.snippet = snippet
                comment.save()
                return redirect('snippet-detail', snippet.id)

