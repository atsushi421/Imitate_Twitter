from django.views.generic.edit import CreateView
from ..models import Tweet

# CreateView は新規作成画面を簡単に作るための View
class TweetView(CreateView):
    template_name = 'tweet.html'
    model = Tweet
    
    # 編集対象にするフィールド
    fields = ["body"]
    
    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super(TweetView, self).form_valid(form)