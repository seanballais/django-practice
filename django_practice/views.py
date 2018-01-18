from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.mail import send_mail

import datetime

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.CharField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())

        if num_words < 4:
            raise forms.ValidationError('Not enough words!')

        return message

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['subject'],
                data['message'],
                data.get('email', 'noreply@example.com'),
                ['sean@seanballais.com'],
            )

            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial={ 'subject': 'I love your site!' }
        )

    return render(request, 'contact_form.html', { 'form': form })

def hello (request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', { 'current_date': now })

def display_meta(request):
    values = request.META.items()
    sorted(values)

    html = []
    for key, value in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(key, value))

    return HttpResponse('<table>{}</table>'.format('\n'.join(html)))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    return render(request, 'hours_ahead.html',
                           { 'offset': offset, 'time': dt })
