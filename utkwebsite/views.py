from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ServiceAward, LetterAward, BoardAward
from .forms import ServiceForm, LetterForm, BoardForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'utkwebsite/index.html', {})

def membership(request):
    return render(request, 'utkwebsite/membership.html', {})

def board(request):
    return render(request, 'utkwebsite/board.html', {})

def letterWinner(request):
    return render(request, 'utkwebsite/letterwinner.html', {})

def serviceAward(request):
    return render(request, 'utkwebsite/service_award.html', {})

def contact(request):
    return render(request, 'utkwebsite/contact.html', {})

def about(request):
    return render(request, 'utkwebsite/about.html', {})

def events(request):
    return render(request, 'utkwebsite/events.html', {})

def service_form(request):
    form = ServiceForm(request.POST)

    if request.method == 'POST':
        # form = RegisterForm(request.POST)
    
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            sport = form.cleaned_data['sport']
            year = form.cleaned_data['year']
            statement = form.cleaned_data['statement']
            nominator = form.cleaned_data['nominator']

            print(full_name)
            print(sport)
            print(year)
            print(statement)
            print(nominator)


            # subject = 'Test Message'
            message = "Full Name: {}, Sport which Nominee lettered in: {}, Year that Nominee graduated: {}, Statement of Support for Nominee: {}, Nominator/Nominated By: {}"            # from_email = email
            # recipients = ['growuppod95@gmail.com',]

            print(message.format(full_name, sport, year, statement, nominator))
            form.save()
            # send_mail(subject, message.format(pickDates, attendees, name, reasons, brand), from_email, recipients, fail_silently = False,)
            return HttpResponseRedirect('/')
    
    else:
        form = ServiceForm()


    return render(request, 'utkwebsite/service_form.html', {'form': form})

def letter_winner_form(request):
    form = LetterForm(request.POST)

    if request.method == 'POST':
        # form = RegisterForm(request.POST)
    
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            relation = form.cleaned_data['relation']
            statement = form.cleaned_data['statement']
            nominator = form.cleaned_data['nominator']

            print(full_name)
            print(relation)
            print(statement)
            print(nominator)


            # subject = 'Test Message'
            message = "Full Name: {}, Nominee’s Relation to University of Tennessee Athletics: {}, Statement of Support for Nominee: {}, Nominator/Nominated By: {}"            # from_email = email
            # recipients = ['growuppod95@gmail.com',]

            print(message.format(full_name, relation, statement, nominator))
            form.save()
            # send_mail(subject, message.format(pickDates, attendees, name, reasons, brand), from_email, recipients, fail_silently = False,)
            return HttpResponseRedirect('/')
    
    else:
        form = LetterForm()


    return render(request, 'utkwebsite/letter_winner_form.html', {'form': form})

def board_form(request):
    form = BoardForm(request.POST)

    if request.method == 'POST':
    
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            sport = form.cleaned_data['sport']
            year = form.cleaned_data['year']
            statement = form.cleaned_data['statement']
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            phone = form.cleaned_data['phone']
            nominator = form.cleaned_data['nominator']

            print(full_name)
            print(sport)
            print(year)
            print(statement)
            print(address_one)
            print(address_two)
            print(city)
            print(state)
            print(zip_code)
            print(phone)
            print(nominator)


            # subject = 'Test Message'
            message = "Full Name: {}, Sport which Nominee lettered in: {}, Year that Nominee graduated: {}, Statement of Support for Nominee: {}, Address 1: {}, Address 2: {},  City: {}, State: {}, Zip Code: {}, Phone: {},  Nominator/Nominated By: {}"
            # recipients = ['growuppod95@gmail.com',]

            print(message.format(full_name, sport, year, statement, address_one, address_two, city, state, zip_code, phone, nominator))
            form.save()
            # send_mail(subject, message.format(pickDates, attendees, name, reasons, brand), from_email, recipients, fail_silently = False,)
            return HttpResponseRedirect('/')
    
    else:
        form = BoardForm()


    return render(request, 'utkwebsite/board_form.html', {'form': form})
