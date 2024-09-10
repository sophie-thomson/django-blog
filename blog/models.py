from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # the slug is what you'll use to build a URL for each of your posts
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    # auto_now_add=True means the default created time is the time of post entry
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=500, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        # - prefix to created_on tells programme to display in descending order
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.post} by {self.author}"

