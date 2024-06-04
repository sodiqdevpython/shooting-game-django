from django.db import models

class MainDB(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{str(self.name1)} | {str(self.name2)}"
    
    class Meta:
        verbose_name = "Ishtirokchi"
        verbose_name_plural = "Ishtirokchilar"