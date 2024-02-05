# annotator/models.py
from django.db import models

class PDFDocument(models.Model):
    file = models.FileField(upload_to='pdfs/')
    class Meta:
        app_label = 'annotator'

class Comment(models.Model):
    pdf = models.ForeignKey(PDFDocument, on_delete=models.CASCADE)
    content = models.TextField()
    x_position = models.FloatField()
    y_position = models.FloatField()

class Picture(models.Model):
    pdf = models.ForeignKey(PDFDocument, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    x_position = models.FloatField()
    y_position = models.FloatField()
