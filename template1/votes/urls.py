from django.urls import path
from . import views


app_name = 'votes'

urlpatterns = [
    # Blogカテゴリの一覧ページのURLパターン
    path('', views.VotesView.as_view(), name='votes'),
]
