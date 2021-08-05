from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from ..models import Tweet, Like


class LikeView(View):
    def post(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=request.POST.get('tweet_id'))
        user = request.user
        liked = False
        like = Like.objects.filter(tweet=tweet, user=user)
        
        if(like.exists()):
            like.delete()
        else:
            like.create(tweet=tweet, user=user)
            liked = True
            
        context={
            'tweet_id': tweet.id,
            'liked': liked,
            'count': tweet.like_set.count(),
        }
        
        return HttpResponseRedirect(reverse('index'))