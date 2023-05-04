from django.db import models

class Midias(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director = models.TextField()
    description = models.TextField()
    created_at = models.DateField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        verbose_name_plural = 'Midias'