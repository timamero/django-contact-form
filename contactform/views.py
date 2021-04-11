from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.mail import message, send_mail, mail_admins

from .models import Contact
from .forms import ContactForm


def index(request):
    """View function for home page of site."""

    # if POST request, process form data
    if request.method == 'POST':
        # Create form instance and populate it with data from the request
        form = ContactForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            form_first_name = form.cleaned_data['first_name']
            form_last_name = form.cleaned_data['last_name']
            form_email = form.cleaned_data['email']
            form_phone = form.cleaned_data['phone']
            # form_date = form.cleaned_data['date']
            form_message = form.cleaned_data['message']
            c = Contact(
                first_name=form_first_name,
                last_name=form_last_name,
                email=form_email,
                phone=form_phone,
                # date=form_date,
                message=form_message
            )
            c.save()

            # Send e-mail to admin
            mail_subject = 'Contact Form Message'
            mail_message = ('Name: ' + form_first_name + ' ' + form_last_name + '\n'
                            'Email: ' + form_email + '\n'
                            'Phone: ' + str(form_phone) + '\n'
                            # 'Date: ' + str(form_date) + '\n'
                            'Message: \n' + form_message
                            )
            mail_admins(
                mail_subject,
                mail_message,
                fail_silently=False
            )

            return HttpResponseRedirect(reverse('success')) # CHANGE LATER, change to success url

    # if GET (or any other method) create blank form
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context=context)


def success_view(request):
    return render(request, 'contactform/success.html')
    