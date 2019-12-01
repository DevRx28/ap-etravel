from django.db import models
import django.core.validators as valid

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=35, unique=True, primary_key=True, validators=[valid.EmailValidator])
	password = models.CharField(max_length=20)
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	userPhone = models.CharField(max_length=14)
	debitNum = models.CharField(max_length=16, null=True)
	creditNum = models.CharField(max_length=16, null=True)


class Location(models.Model):
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	region = models.CharField(max_length=2)
	image = models.CharField(max_length=200)

class History(models.Model):
	userEmail = models.CharField(max_length=36)
	BOOKING_TYPES = [('flight', 'Flight'), ('hotel', 'Hotel')]
	bookingType = models.CharField(choices=BOOKING_TYPES, max_length=6)
	bookingDate = models.DateField()
	payment = models.DecimalField(max_digits=6,decimal_places=2)
	paymentDetails = models.CharField(max_length=16)
	companyName = models.CharField(max_length=30, default='company')
	location = models.CharField(max_length=30, default='location')

class Flight(models.Model):
	carrierName = models.CharField(max_length=30)
	origin = models.CharField(max_length=30)
	layover = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	remainingSeatsEconomy = models.IntegerField()
	remainingSeatsBusiness = models.IntegerField()
	remainingSeatsFirst = models.IntegerField()

class Hotel(models.Model):
	rent = models.DecimalField(max_digits=6,decimal_places=2)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	brand = models.CharField(max_length=30,default='hotel')
	rating = models.IntegerField(default=0)

class Payment(models.Model):
	PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
	paymentAmount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
	cardNumber = models.CharField(max_length=16)
