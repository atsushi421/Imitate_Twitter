from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from . import Tweet

User = get_user_model()

class Like(models.Model):
    # いいねしたユーザ
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    # 対象の Tweet
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE
    )
    
    # 新規いいねした後に、飛ぶリンク
    def get_absolute_url(self):
        return reverse_lazy('index')