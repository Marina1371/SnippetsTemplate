from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/create', views.snippets_page, name='snippets-create'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippets-delete'),
    path('snippet/<int:id>', views.snippet, name='snippets-data'),
    path('snippet/<int:snippet_id>', views.snippet_detail, name='snippet-detail' ),
    path('snippet/<int:snippet_id>/edit', views.snippet_edit, name='snippet-edit'),
    path('test', views.test)
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
