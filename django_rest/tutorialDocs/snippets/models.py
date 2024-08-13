from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Programming')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField( default='python', max_length=100)
    style = models.CharField( default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
