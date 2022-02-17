from pyexpat import model
from django.db import models

# Create your models here.
class Subjects(models.Model):
    title = models.CharField(max_length=50)
    imgurl = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_slug(self):
        return str(self.title).lower().replace(' ','-')

    def get_absolute_url(self):
        return f'subjects/{self.get_slug()}/'


class Papers(models.Model):
    title = models.CharField(max_length=50)
    imgurl = models.TextField()
    fileurl = models.TextField()
    slug = models.SlugField()
    subject = models.ForeignKey(
        Subjects, related_name='papers', on_delete=models.CASCADE)

    def get_slug(self):
        return str(self.title).lower().replace(' ','-')

    def get_absolute_url(self):
        return f'papers/{self.get_slug()}'