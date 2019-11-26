from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(request.POST)
            print(form.cleaned_data['email'])
            form.save()
            # redirect to a new URL:
            return render(request, 'simple_form/thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'simple_form/contact.html', {'form': form})
