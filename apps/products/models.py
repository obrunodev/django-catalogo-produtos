from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel
from django.utils.text import slugify


class Product(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField("slug", max_length=255, blank=True)
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)
    value = models.DecimalField("Valor", decimal_places=2, max_digits=10)
    promotional_value = models.DecimalField("Valor promocional",
                                            decimal_places=2,
                                            max_digits=10,
                                            blank=True,
                                            null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            counter = 1
            while Product.objects.filter(
                slug=self.slug
            ).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
