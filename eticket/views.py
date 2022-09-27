from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *
import qrcode


def Home(request):
    return render(request, 'Home.html')


def About(request):
    return render(request, 'About.html')


def Services(request):
    return render(request, 'Services.html')


def Book(request):
    return render(request, 'Booking.html')


def success(request):
    return render(request, 'success.html')


def ngma(request):
    return render(request, 'NGMA.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                return redirect('/')
            else:
                error = "Invalid username or password!!"
        except:
            error = "Invalid username or password!!"
    d = {'error': error}
    return render(request, 'Login.html', d)


def Register(request):
    error = ""
    if request.method == 'POST':
        us = request.POST['username']
        e = request.POST['email']
        pd = request.POST['password']
        ad = request.POST['address']
        nat = request.POST['nationality']
        do = request.POST['dob']
        c = request.POST['phone']
        g = request.POST['gender']
        try:
            user = User.objects.create_user(
                username=us, password=pd, email=e)
            Visitor.objects.create(
                user=user, nationality=nat, dob=do, phone=c, address=ad, gender=g)

            user = authenticate(username=us, password=pd)
            login(request, user)
            return redirect('/')
        except:
            error = "Unable to register!!"
    d = {'error': error}
    return render(request, 'Register.html', d)


def Booking(request):
    error = ""
    # if not request.user:
    #     return redirect('register')
    # ticket = Booking_Detail.objects.all()
    if request.method == 'POST':

        # us = request.POST['username']
        # e = request.POST['email']
        # pd = request.POST['password']
        mn = request.POST['museumname']
        dv = request.POST['dov']
        t = request.POST['time']
        nb = request.POST['nob']
        ua = User.objects.filter(username=request.user.username).first()
        try:

            Booking_Detail.objects.create(
                user=ua,
                museumname=mn, dov=dv, time=t, nob=nb)
            # ti = Booking_Detail.filter(id=request.booking_detail.id).first()
            # img = qrcode.make(ti)
            # qname = "code/"+str(ti)+".png"
            # qcode = qname.save(qname, "png")

            error = "no"
            return redirect('/success')

        except:
            error = "yes"
            d = {'error': error}
            return render(request, 'Booking.html', d)


def Ticket(request):
    return render(request, 'eticket.html')


# def Ticket(request):
#     # un = Booking_Detail.objects.get(username=request.user.username).first()
#     # no = Booking_Detail.objects.get(nob=request.Booking_Detail.nob)
#     # dv = Booking_Detail.objects.get(dov=request.Booking_Detail.dov)
#     # mn = Booking_Detail.objects.get(
#     #     museumname=request.booking_detail.museumname)
#     error = ""
#     bd = Booking_Detail.objects.filter(id= )
#     u = User.objects.get(id)
#     img = qrcode.make(bd)
#     qname = "code/"+str(bd)+".png"
#     qcode = qname.save(qname, "png")
#     try:

#         Ticket.objects.create(
#             user=u, booking_detail=bd,
#             qrcode=qcode)
#         et = Ticket.objects.get()
#         error = "no"
#         return redirect('/eticket')
#     except:
#         error = "yes"
#         d = {'error': error}
#         return render(request, 'Booking.html, d')
