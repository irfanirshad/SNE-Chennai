# pylint: disable=missing-function-docstring
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

'''
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os
'''

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
    
    # Check if user has already made inquiry
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(request, 'You have already made inquiry for this listing')
            return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
    
    contact.save()
    
    
    send_mail(
        'Property Listing Inquiry NOTIFICATION From WEBSITE',
        'There has been an inquiry for ' + listing + '. Sign into the admin panel for more information',
        'sne_website_bot@gmail.com',
        [realtor_email, 'snechennai.bot@gmail.com'],
        fail_silently=False
    )
    
    messages.success(request, 'Your request has been submitted. An executive will get back to you soon')
    return redirect('/listings/'+listing_id)
    
    
