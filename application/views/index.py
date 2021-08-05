from django.views.generic import ListView
from ..models import Tweet

# ListView は一覧を簡単につくれる
class IndexView(ListView):
    template_name='index.html'
    
    # 一覧するモデルを指定. object_list で取得可能
    model = Tweet
    
    # model を呼び出すメソッド
    def get_queryset(self):
        return Tweet.objects.order_by('-id')  # 新しい順