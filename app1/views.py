from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, RestorePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import time, date, datetime
import datetime as dt
from qrcode import *

from PIL import Image
import random
import math
from .models import *
from django.http import HttpResponse

import razorpay
import smtplib


# Create your views here.
ava_bike = None


def home(request):
    return render(request, 'home.html')


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url="loginPage")
def rent_now(request):

    print(request.POST.get('startDate2'))
    if request.method == 'POST':

        dic = {
            'location': '',
            'sth': '',
            'stm': '',
            'eth': '',
            'etm': '',
            'bike': ''
        }

        loc = request.POST.get('loc')
        dic['location'] = loc

        x = (request.POST.get('startDate2'))
        if x == "":
            print('Missing start Date')
        if x != "":
            x = request.POST.get('startDate2').split(':')
            if x[0].startswith('0'):
                x[0] = x[0][1]
            if x[1].startswith('0'):
                x[1] = x[1][1]
            h = int(x[0])
            m = int(x[1])
            s = 0
            starttime = time(h, m, s)
            dic['sth'] = h
            dic['stm'] = m

        y = (request.POST.get('endDate2'))
        if y != "":
            y = request.POST.get('endDate2').split(':')
            if y[0].startswith('0'):
                y[0] = y[0][1]
            if y[1].startswith('0'):
                y[1] = y[1][1]
            h = int(y[0])
            m = int(y[1])
            s = 0
            endtime = time(h, m, s)
            dic['eth'] = h
            dic['etm'] = m
        bike = request.POST.get('choose_bike')
        dic['bike'] = bike

        flag = 0

        for i in dic:
            if dic[i] == '' or dic['location'] == 'Pick Location' or dic['bike'] == 'Choose Bike':
                flag = 1

        if flag == 1:
            messages.info(
                request, 'Select complete details (Location, time (from , to), Bike)')
        elif flag == 0:
            duration = (datetime.combine(date.today(), endtime) -
                        datetime.combine(date.today(), starttime))
            x = (str(duration).split(":")[0])
            if x.startswith('-'):
                duration = 0
            else:
                duration = int(x)

            ava_bike = Available_Bikes.objects.get(
                name=dic['bike'], location=dic['location'])
            count = ava_bike.number

            if duration < 1:
                messages.info(
                    request, 'Time Duration should be more than one hour')

            elif count < 1 or ava_bike == 'None':
                messages.info(
                    request, dic['bike'] + ' is not available at ' + dic['location'] + ' centre')

            else:
                l = list(dic.values())

                if (dic['bike'] == 'Deluxe'):
                    amount = 20
                    extra_charges = 40
                elif (dic['bike'] == 'Splendor Plus'):
                    amount = 25
                    extra_charges = 45
                elif (dic['bike'] == 'Pleasure'):
                    amount = 30
                    extra_charges = 50
                elif (dic['bike'] == 'Passion Pro'):
                    amount = 35
                    extra_charges = 55
                elif (dic['bike'] == 'Royal Enfield 200CC'):
                    amount = 60
                    extra_charges = 80

                l.append(amount * duration)
                l.append(extra_charges)
                response = redirect('create_order', l)

                # print(Available_Bikes.objects.get(name=dic['bike'],location=dic['location']))
                # print(Rented_Bikes.objects.get(username="Nikhil183",bike='\"\'Passion Pro\'\"'))
                return response

    return render(request, 'rent_now.html')


def create_order(request, l):
    client = razorpay.Client(auth=("Key_ID", "SECRET_KEY"))
    context = {}
    order_currency = 'INR'
    order_receipt = 'UNIQUE_ORDER_RECEIPT'
    notes = {
        'YOURNOTES': 'XXXX'}
    order_amount = l[-1] + l[-2]
    response = client.order.create(dict(
        amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0'))
    order_id = response['id']
    order_status = response['status']

    if order_status == 'created':
        context['product_id'] = product
        context['price'] = order_amount
        context['name'] = name
        context['phone'] = phone
        context['email'] = email
        context['order_id'] = order_id

        return render(request, 'confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')


def payment_status(request):

    response = request.POST

    params_dict = {
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'invoice.html', [])
    except:
        return render(request, 'invoice.html', [])


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'login.html')

# .....sending mail..................................


def send_mail(sender_email, password, recievers_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
    server.ehlo()
    # encrypts the connnection
    server.starttls()

    server.login(sender_email, password)
    subject = 'Sucessfully Registered'
    body = 'Welcome to Cityon Bikes !! '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        sender_email,
        recievers_email,
        msg
    )
    server.quit()
# ..........................................................


def forgotPassword(request):
        form = RestorePasswordForm()

        if request.method == 'POST':
            form = RestorePasswordForm(request.POST)

            if form.is_valid():                
                email = form.cleaned_data.get('email')
#                 send_mail("senders email",
#                           "password", str(email))
                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'forgot_password.html', context)


def register(request):
    if request.user.is_authenticated:

        return redirect('rent_now')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account created for " + user)
                email = form.cleaned_data.get('email')
#                 send_mail("senders email",
#                           "password", str(email))
                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'register.html', context)


def Employeedata(request):
    return render(request, 'regex.html')


def invoice(request, dic):

    if request.method == 'POST':
        OTP = random.randint(100000, 999999)
        img = make("OTP :" + str(OTP))
        img.save(r"static/images/test.jpg")
        context = {
            'message': OTP,
        }
        dic = dic[1:-1]
        dic = dic.split(', ')
        print(dic)
        dic.append(OTP)

        return redirect('paymentDone', dic)

    dic = dic[1:-1]
    # print(dic)
    l = dic.split(',')
    dic = l
    # print(l)

    starttime = time(int(l[1]), int(l[2]))
    endtime = time(int(l[3]), int(l[4]))

    context = {
        'starttime': starttime,
        'endtime': endtime,
        'loc': l[0],
        'bike': l[5],
        'amount': l[6],
        'extra_charges': l[7],
    }

    return render(request, "invoice.html", context)


def paymentDone(request, dic):
    dic = dic[1:-1]
    dic = dic.split(', ')
    context = {
        'otp': dic[8]
    }

    starttime = time(int(dic[1][1:-1]), int(dic[2][1:-1]))
    endtime = time(int(dic[3][1:-1]), int(dic[4][1:-1]))

    rented_bike = Rented_Bikes()
    rented_bike.username = str(request.user)
    rented_bike.location = dic[0][2:-2]
    rented_bike.start_time = starttime
    rented_bike.end_time = endtime
    rented_bike.bike = dic[5][2:-2]
    rented_bike.amount = int(dic[6][1:-1])
    rented_bike.otp = dic[8]
    rented_bike.save()

    # print(dic[0][2:-2])
    # print(Available_Bikes.objects.get(name=dic[5],location=dic[0]))
    ava_bike = Available_Bikes.objects.get(
        name=rented_bike.bike, location=rented_bike.location)
    ava_bike.number -= 1
    ava_bike.save()

    return render(request, "qrcode_page.html", context)


def about(request):

    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def offer(request):
    return render(request, 'offer.html')
