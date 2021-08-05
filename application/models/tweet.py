from django.db import models
from django.urls import reverse_lazy
from . import User

class Tweet(models.Model):
    # この Tweet を投稿した人
    poster = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # 投稿者のアカウントが削除されたら、Tweet も一緒に消す
        blank = False,
        null = False
    )
    
    # 投稿日
    created = models.DateTimeField(
        auto_now_add = True,  # モデルを新規追加した時に時刻を取得し、格納
        editable = False,  # ユーザが編集できるかどうか
        blank = False,
        null = False
    )
    
    # 内容
    body = models.TextField(
        blank = True,
        null = False
    )
    
    # 新規ツイートした後に、飛ぶリンク
    def get_absolute_url(self):
        return reverse_lazy('index')