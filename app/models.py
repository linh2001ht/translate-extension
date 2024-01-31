from django.db import models

# Create your models here.
class Dict(models.Model):
    lang = models.CharField(max_length=10)
    origi = models.TextField()
    dic = models.TextField()
    class Meta:
        db_table = "dict"