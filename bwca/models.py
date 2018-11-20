from django.db import models
from django.utils.text import slugify
from django.urls import reverse

import uuid

# Create your models here.
class Camper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank = True)

    ROLE_CHOICES = (
        ('Scout', 'Scout'),
        ('Parent', 'Parent')
    )

    COMMIT_CHOICES = (
        ('Interested', 'Interested'),
        ('Committed', 'Committed'),
        ('Cannot_Attend', 'Cannot Attend')
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    commitment = models.CharField(max_length=30, choices=COMMIT_CHOICES)
    week1 = models.BooleanField("Jul 30 - Jul 6")
    week2 = models.BooleanField("Jul 7 - Jul 13")
    week3 = models.BooleanField("Jul 14 - Jul 20")
    week4 = models.BooleanField("Jul 21 - Jul 27")
    week5 = models.BooleanField("Jul 28 - Aug 3")
    week6 = models.BooleanField("Aug 4 - Aug 10")
    week7 = models.BooleanField("Aug 11 - Aug 17")
    week8 = models.BooleanField("Aug 18 - Aug 24")
    notes = models.CharField(max_length=200, null=True, blank = True)
    slug = models.SlugField(unique=False, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{str(self.first_name) + " " + str(self.last_name)}'

    def save(self):
        self.slug = slugify(self.first_name +" " + self.last_name)
        super(Camper, self).save()

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('camperdetail', args=[str(self.slug)])


class Outfitter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    website = models.URLField()
    slug = models.SlugField(unique=False, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{str(self.name)}'

    def save(self):
        self.slug = slugify(self.name +" " + self.name)
        super(Outfitter, self).save()

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('outfitterdetail', args=[str(self.name)])


class Gear(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    notes = models.CharField(max_length=200)

    CATEGORY_CHOICES = (
        ('Required', 'Required'),
        ('Recommended', 'Recommended'),
        ('Optional', 'Optional')
            )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)




