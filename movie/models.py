from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    

    class Meta:
        verbose_name = "Mi modelo"
        verbose_name_plural = "Mis modelos"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    

    class Meta:
        verbose_name = "Mi modelo"
        verbose_name_plural = "Mis modelos"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})
    
