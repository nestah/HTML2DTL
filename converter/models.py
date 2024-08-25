from django.db import models

# Create your models here.
class HTMLFile(models.Model):
    file = models.FileField(upload_to='html_files/')
    uploaded_at= models.DateTimeField(auto_now_add=True)