from django.db import models
from django.utils.text import slugify

def image_upload(instance, filename):
    image_name, extension = filename.split('.')
    return '%s/%s/%s.%s'%('images',instance.__class__.__name__,image_name, extension)

# Create your models here.
class Service(models.Model):
    service_name = models.CharField('service_name', max_length= 60)
    service_bio = models.CharField('service_bio', max_length = 225)
    service_disc = models.CharField('service_disc', max_length = 420)
    service_logo = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank = True, null = True)

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.service_name)
        super(Service, self).save(*args, **kwargs)
