from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.JSONField(null=True, blank=True)
    price = models.IntegerField()
    img_path = models.URLField(null=True, blank=True)
    def get_description(self, description:dict):
        self.description = description
    def remove_description(self):
        self.description = None
    def get_img_path(self, img_path:str):
        self.img_path = img_path
    def remove_img_path(self):
        self.img_path = None