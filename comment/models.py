from django.db import models

from account.models import MyUser
from main.models import Post


class Comment(models.Model):
    title = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
