from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    analysis_result = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
