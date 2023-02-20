from django.db import models
from PIL import Image
from django.conf import settings
from django.urls import reverse
import os
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .utils import generate_ref_code
from mptt.models import MPTTModel, TreeForeignKey


def product_image_location(instance, filename):
    file_path = 'product_img_api/{uuid}.jpeg'.format(
    uuid = generate_ref_code(), filename=filename
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path


class Category(MPTTModel):
    category_name = models.CharField(max_length=100, null=True, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category_parent')
    date_created = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

    class MPTTMeta:
        order_insertion_by = ['date_created']

    def __str__(self):
        full_path = [self.category_name]
        p = self.parent
        while p is not None:
            full_path.append(p.category_name)
            p = p.parent
        return ' -> '.join(full_path[::-1])
        

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(verbose_name="describe_product", blank=True)
    product_image = models.ImageField(upload_to=product_image_location, null=True, blank=True)
    slug = AutoSlugField(populate_from="product_name", unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('product_api:product', args=[self.slug])        

    @property
    def product_image_url(self):
        try:
            url = self.product_image.url
        except:
            url = ""

        return url

    def __str__(self):
        return self.product_name


@receiver(post_save, sender=Product)
def save_img(sender, instance, *args, **kwargs):
    SIZE = 600, 600
    if instance.product_image:
        pic = Image.open(instance.product_image.path)
        try:
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(instance.product_image.path)
        except:
            if pic.mode in ("RGBA", 'P'):
                blog_pic = pic.convert("RGB")
                blog_pic.thumbnail(SIZE, Image.LANCZOS)
                blog_pic.save(instance.product_image.path) 

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.product_image.delete(False)