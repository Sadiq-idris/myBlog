from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    tags = (
        ("tech", "Tech"),
        ("entertainment", "Entertainment"),
        ("sport", "Sport"),
        ("news", "News"),
        ("health", "Health"),
        ("tricks", "Tricks"),
    )

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="PostThumbnail")
    date = models.DateTimeField(default=timezone.now)
    conclusion = models.TextField(max_length=2000)
    tag = models.CharField(max_length=200, choices=tags, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args = [str(self.pk)])


class Comment(models.Model):
    comment_username = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    comment = models.CharField( max_length=100)

    def __str__(self):
        return self.comment