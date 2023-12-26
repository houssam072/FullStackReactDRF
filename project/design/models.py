from django.db import models

# Create your models here.
def image_upload(instance, filename):
    image_name, extension = filename.split('.')
    return '%s/%s/%s.%s'%('images',instance.__class__.__name__, image_name, extension)
    pass
class Design(models.Model):
    title = models.CharField(max_length = 120)
    image_bio = models.ImageField(upload_to= image_upload)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class DesignImages(models.Model):
    design = models.ForeignKey(Design, on_delete = models.CASCADE)
    images = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.design.title