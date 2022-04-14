from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    author = models.CharField(max_length=10, default="Name")

    def __str__(self):
        return self.title + " / " + self.author