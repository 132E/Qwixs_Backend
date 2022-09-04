from django.db import models

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Business(models.Model):
    name = models.CharField(max_length=150)
    about = models.CharField(max_length=400, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=2, default=' ')
    zipcode = models.CharField(max_length=6, default=' ')
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='businesses')

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name
