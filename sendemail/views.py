from django.shortcuts import render

# Create your views here.
# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['boomentrepreneurship@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "You have successfully logged in!")
            messages.success(request, "Thanks for your email!")
            return redirect('email_success')
    return render(request, "contact_us.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')