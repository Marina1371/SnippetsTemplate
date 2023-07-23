from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views
from django.contrib import admin


urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippets-delete'),
    # path('snippet/<int:id>', views.snippet, name='snippets-data'),
    path('snippet/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippet/<int:snippet_id>/edit', views.snippet_edit, name='snippet-edit'),
    path('snippet/my', views.snippet_my, name='snippets-my'),
    path('snippet/<int:pk>/comment', views.comment_add, name='snippet-comment'),
    path('register', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('test', views.test),
    path('admin/', admin.site.urls),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
