from django.db import models

class department(models.Model):
    description = models.TextField()
    rooms = models.TextField()
    monthly_amount = models.TextField()
    guarantee = models.IntegerField()
    floor = models.IntegerField()
    bathroom = models.IntegerField()
    photos = models.TextField()
    state = models.TextField()
    pets = models.BooleanField()
    kids = models.BooleanField()
    parking = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

"""class Owner(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.IntegerField()
    telephone = models.IntegerField()

class User(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name