from django.db import models
from utils.minio import minio
from django.contrib.auth import get_user_model

class Ml_model(models.Model):
    name = models.TextField(blank=False, null=True)
    model_name = models.TextField(blank=False, null=True)
    username = models.TextField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    version = models.FloatField(blank=False, null=True)
    eval_metrics = models.TextField(blank=False, null=True)
    columns = models.TextField(blank=False, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="+", blank=True)
    purchased = models.ManyToManyField(get_user_model(), blank=True)

    class Meta:
        db_table = "ml_models"
        
    def __str__(self):
        return self.name

    def download(model_name, path):
        return minio.download('deployed-objects', model_name, path)