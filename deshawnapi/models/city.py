from django.db import models  # Import base class from Django stdlib


class City(models.Model):  # Must inherit from this base class
    name = models.CharField(max_length=155)  # Define all non-id fields
