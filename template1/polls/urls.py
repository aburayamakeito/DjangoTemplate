from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    # Blogカテゴリの一覧ページのURLパターン
    path('', views.PollsView.as_view(), name='polls'),
]
