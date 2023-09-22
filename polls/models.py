from django.db import models

# Create your models here.
class NewsModel(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name