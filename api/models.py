from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image

# Create your models here.

base_url = 'http://127.0.0.1:8000/'


class Subjects(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(
        upload_to='staticfiles/img/', blank=True, null=True)
    thumbnail = models.FileField(
        upload_to='staticfiles/img/', blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_slug(self):
        self.slug = str(self.title).lower().replace(' ', '-')
        self.save()
        return self.slug

    def get_absolute_url(self):
        return f'subject/{self.get_slug()}/'

    def get_image(self):
        if self.image:
            return base_url + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return base_url + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return base_url + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img = img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Papers(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.FileField(
        upload_to='staticfiles/img/', blank=True, null=True)
    file = models.FileField(upload_to='staticfiles/files/')
    slug = models.SlugField()
    subject = models.ForeignKey(
        Subjects, related_name='papers', on_delete=models.CASCADE)

    def get_slug(self):
        return str(self.title).lower().replace(' ', '-')

    def get_file(self):
        if self.file:
            return base_url + self.file.url
        return ""

    def get_absolute_url(self):
        return f'papers/{self.get_slug()}'
