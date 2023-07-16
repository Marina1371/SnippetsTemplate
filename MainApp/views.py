from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('snippets-list')

    return render(request, 'pages/add_snippet.html', {"form": form, "pagename": "Create Snippet"})


def snippets_page(request):
    items = Snippet.objects.all()
    return render(request, 'pages/view_snippets.html', {"items": items, "pagename": "List Snippets"})


def snippet(request, id):
    snippet = Snippet.objects.get(pk=id)
    return render(request, 'pages/snippet.html', {"item": snippet, "pagename": "View Snippet"})


def test(request):
    return render(request, 'demo_bs.html')
