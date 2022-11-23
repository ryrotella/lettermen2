from django.db import models
from django import forms
from .validators import validate_name, validate_brand
from django.core.validators import MinLengthValidator

# Create your models here.
class AthImage(models.Model):
    image = models.ImageField(upload_to = 'gallery/')


class ServiceAward(models.Model):
    full_name = models.CharField(max_length=50) # validators=[validate_name]
    sport = models.CharField(max_length=30) #validators=[validate_sport]
    year = models.CharField(max_length=4) #validators=[validate_year]
    # email = models.EmailField()
    statement = models.TextField(blank=False)
    nominator = models.CharField(max_length=50) #validators=[validate_name]

    def __str__(self):
        message = "Full Name: {}, Sport which Nominee lettered in: {}, Year that Nominee graduated: {}, Statement of Support for Nominee: {}, Nominator/Nominated By: {}"
        return message.format(self.full_name, self.sport, self.year, self.statement, self.nominator)


class LetterAward(models.Model):
    full_name = models.CharField(max_length=50) # validators=[validate_name]
    relation = models.CharField(max_length=200) #validators=[validate_relation]
    # email = models.EmailField()
    statement = models.TextField(blank=False)
    nominator = models.CharField(max_length=50) #validators=[validate_name]

    def __str__(self):
        message = "Full Name: {}, Nominee’s Relation to University of Tennessee Athletics: {}, Statement of Support for Nominee: {}, Nominator/Nominated By: {}"
        return message.format(self.full_name, self.relation, self.statement, self.nominator)

class BoardAward(models.Model):
    full_name = models.CharField(max_length=50) # validators=[validate_name]
    sport = models.CharField(max_length=30) #validators=[validate_sport]
    year = models.CharField(max_length=4) #validators=[validate_year]
    # email = models.EmailField()
    statement = models.TextField(blank=False)
    address_one = models.CharField(max_length=50)
    address_two = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    nominator = models.CharField(max_length=50) #validators=[validate_name]

    def __str__(self):
        message = "Full Name: {}, Sport which Nominee lettered in: {}, Year that Nominee graduated: {}, Statement of Support for Nominee: {}, Address 1: {}, Address 2: {},  City: {}, State: {}, Zip Code: {}, Phone: {}, Nominator/Nominated By: {}"
        return message.format(self.full_name, self.sport, self.year, self.statement, self.address_one, self.address_two, self.city, self.state, self.zip_code, self.phone, self.nominator)