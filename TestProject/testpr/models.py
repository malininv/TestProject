from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(unique=True)

    # category_parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)

    # class Meta:
    # unique_together = ('slug', 'parent',)
    # verbose_name_plural = "categories"

    # def __str__(self):
    #     full_path = [self.name]
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent
    #
    #     return ' -> '.join(full_path[::-1])
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_slug = models.SlugField(unique=True)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_img = models.CharField(max_length=200, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return self.product_name
