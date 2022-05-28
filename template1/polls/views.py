from django.shortcuts import render
from django.views.generic import View, ListView


class PollsView(View):
    """ビュー

    """
    initial = {}
    ctx = {}
    # polls.htmlをレンダリングする
    template_name = 'polls.html'

    # オブジェクト名を polls に指定
    context_object_name = 'polls'

    def get(self, request, *args, **kwargs):

        # 変数を設定
        self.ctx['page'] = 'polls'
        self.ctx['css'] = 'css/base.css'
        self.ctx['js'] = 'js/base.js'

        return render(request, self.template_name, self.ctx)
