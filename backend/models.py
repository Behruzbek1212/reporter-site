from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    rasm = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi
