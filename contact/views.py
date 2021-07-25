from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def contactform(r):
    if r.method == 'POST':
        form = ContactForm(r.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']

            try:
                send_mail(name, message, email,
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("success")

    form = ContactForm()
    return render(r, "contact/contactform.html", {'form': form})


def success(r):
    return render(r, 'contact/success.html')
