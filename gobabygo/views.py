from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import jwt
import datetime

from .models import *



@csrf_exempt
def flights_page(request):
	if request.method == 'POST':
		origin = request.POST['origin'].split(',')
		city = origin[0];
		destination = request.POST['destination'].split(',')
		destinationCity = destination[0];
		startdate = request.POST['startdate']
		startdate = startdate.split('-')
		year = int(startdate[0])
		month = int(startdate[1])
		day = int(startdate[2])
		flightClass = request.POST['class']
		print(request.POST)
		if (flightClass == 'economy'):
			flights = Flight.objects.filter(origin=city).filter(destination=destinationCity).filter(
				departureDate=datetime.date(year, month, day)).filter(remainingSeatsEconomy__gt=0)
			flights = list(flights)
			context = {
                        'results': 'yes',
						'some_list': flights,
                        'class': flightClass
                    }
			return render(request, 'flights.html', context)
		elif (flightClass == 'business'):	
			flights = Flight.objects.filter(origin=city).filter(destination=destinationCity).filter(
				departureDate=datetime.date(year, month, day)).filter(remainingSeatsBusiness__gt=0)
			flights = list(flights)
			context = {
                        'results': 'yes',
						'some_list': flights,
                        'class': flightClass
                    }
			return render(request, 'flights.html', context)
		else:
			flights = Flight.objects.filter(origin=city).filter(destination=destinationCity).filter(
				departureDate=datetime.date(year, month, day)).filter(remainingSeatsFirst__gt=0)
			flights = list(flights)
			context = {
                        'results': 'yes',
						'some_list': flights,
                        'class': flightClass
                    }
			return render(request, 'flights.html', context)
	else:
		return render(request, 'flights.html')	

@csrf_exempt
def login_page(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		authentication_check = User.objects.filter(email = email)
		valid_user = (len(list(authentication_check)) > 0)
		if (valid_user):
			request.session['current_user'] = email
			# request.session['user_name'] = username
			context = {'msg': 'Login was successful!'}
			return render(request, 'login.html', context)
		else:
			context = {'msg': 'Login Failed! Please try again!'}
			return render(request, 'login.html', context)
	else:
		return render(request, 'login.html')

@csrf_exempt
def signup_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		existing_entries = User.objects.filter(email = email)
		unique_user = (len(list(existing_entries)) == 0)
		if (unique_user):
			new_user = User.objects.create(username=username, email=email, password=password)
			new_user.save()
			context = {'msg': 'You have Signed Up successfully!'}
			return render(request, 'signup.html', context)
		else:
			context = {'msg': 'This email is already in use with an account! Please use another email to sign up.'}
			return render(request, 'signup.html', context)
	else:
		return render(request, 'signup.html')

def get_city(loc):
	tokens = loc.split(',')
	return tokens[0]

@csrf_exempt
def hotels_page(request):
	if request.method == 'POST':
		city = get_city(request.POST['location'])
		date_start = request.POST['startdate']
		date_end = request.POST['enddate']
		hotels = Hotel.objects.filter(city = city)
		hotel_list = list(hotels)
		context = {
			'results': 'yes',
			'some_list': hotel_list
		}
		return render(request, 'hotels.html', context)
	else:
		return render(request, 'hotels.html')

def arrange_flight(flightClass, tID, user, bookType, curr_date, card):
    options = Flight.objects.filter(id=tID)
    choice = options.first()
    if (flightClass == 'economy'):
        plane = Flight.objects.filter(id=tID)
        plane.update(remainingSeatsEconomy=choice.remainingSeatsEconomy-1)
        new_transaction = History.objects.create(userEmail=user, bookingType=bookType, bookingDate=curr_date,
                                                 payment=choice.fareEconomy, paymentDetails=card, companyName=choice.carrierName, location=choice.destination)
        new_transaction.save()
    elif (flightClass == 'business'):
        plane = Flight.objects.filter(id=tID)
        plane.update(remainingSeatsBusiness=choice.remainingSeatsBusiness-1)
        new_transaction = History.objects.create(userEmail=user, bookingType=bookType, bookingDate=curr_date,
                                                 payment=choice.fareBusiness, paymentDetails=card, companyName=choice.carrierName, location=choice.destination)
        new_transaction.save()
    elif (flightClass == 'first'):
        plane = Flight.objects.filter(id=tID)
        plane.update(remainingSeatsFirst=choice.remainingSeatsFirst-1)
        new_transaction = History.objects.create(userEmail=user, bookingType=bookType, bookingDate=curr_date,
                                                 payment=choice.fareFirst, paymentDetails=card, companyName=choice.carrierName, location=choice.destination)
        new_transaction.save()

def arrange_hotel(tID, user, bookType, curr_date, card):
    options = Hotel.objects.filter(id=tID)
    choice = options.first()
    new_transaction = History.objects.create(userEmail=user, bookingType=bookType, bookingDate=curr_date,
                                             payment=choice.rent, paymentDetails=card, companyName=choice.brand, location=choice.address)
    new_transaction.save()

def booking_page(request):
	if request.method == 'POST':
		tID = request.GET.get('id')
		bookType = request.GET.get('type')
		card_number = request.POST['card_number']
		card_type = request.POST['card_type']
		user = request.session['current_user']
		curr_date = datetime.datetime.today().strftime('%Y-%m-%d')

		if (bookType == 'flight'):
			flightClass = request.GET.get('class')
			arrange_flight(flightClass, tID, user, bookType, curr_date, card_number)
		elif (bookType == 'hotels'):
			arrange_hotel(tID, user, bookType, curr_date, card_number)
		
		context = {'msg':'Your booking was successful!'}
		return render(request, 'book.html', context)
	else:
		tID = request.GET.get('id')
		bookType = request.GET.get('type')
		if (bookType == 'flight'):
			flightClass = request.GET.get('class')
			choice = Flight.objects.filter(id=tID)
			context = {
				'booking': 'yes',
				'some_list': choice,
				'type': bookType,
				'class': flightClass
			}
			return render(request, 'book.html', context)
		elif (bookType == 'hotel'):
			choice = Hotel.objects.filter(id=tID)
			context = {
				'booking': 'yes',
				'some_list': choice,
				'type': bookType
			}
			return render(request, 'book.html', context)
		else:
			return render(request, 'book.html')

def account(request):
	setting = request.GET.get('setting')
	current_user = request.session['current_user']
	if (setting == 'history'):
		history = History.objects.filter(userEmail=current_user)
		return render(request, 'account.html', {'setting': setting, 'transactions': history})
	else:
		userinfo = User.objects.filter(email=current_user)
		return render(request, 'account.html', {'setting': setting, 'userinfo': userinfo})

def logout(request):
	del request.session['current_user']
	context = {'msg': 'You have logged out successfully!'}
	return render(request, 'login.html', context)

def home_page(request):
	return render(request, 'index.html')