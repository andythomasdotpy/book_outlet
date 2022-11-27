from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

    


class Address(models.Model):
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.street_number} {self.street_name} {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(
        Address, 
        on_delete=models.CASCADE,
        null=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Author Info"
    

class Book(models.Model):
    # Django automatically adds id column with auto-incrementing column
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    country = models.ManyToManyField(Country, null=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.title} ({self.rating})"