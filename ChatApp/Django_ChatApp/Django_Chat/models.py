from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    displayName = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="email", max_length=200, unique=True)
    uID = models.CharField(max_length=28, unique=True)


class Sub_Tuck(models.Model):
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    text = models.TextField()
    poster = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE, null=True)
    voters = models.ManyToManyField(User, related_name="pvoters")
    votes = models.IntegerField(0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    text = models.TextField()
    poster = models.ForeignKey(User, related_name="reply", on_delete=models.CASCADE)
    voters = models.ManyToManyField(User, related_name="rvoters")
    votes = models.IntegerField(0)
    repliedTo = models.ForeignKey(Post, related_name="replies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
