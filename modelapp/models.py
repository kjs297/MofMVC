from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, help_text='최대 100자 내외')
    content = models.TextField()
    tag = models.CharField(max_length=50, blank=True, help_text='문재인당선')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title