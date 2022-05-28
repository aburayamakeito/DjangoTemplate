from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView


class VotesView(TemplateView):
    """ビュー

    """
    # vote.htmlをレンダリングする
    template_name = 'votes/votes.html'

    # オブジェクト名を votes に指定
    context_object_name = 'votes'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # 変数を設定
        ctx['page'] = 'votes'
        ctx['css'] = 'css/votes.css'
        ctx['js'] = 'js/votes.js'

        return ctx
