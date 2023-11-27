from django.shortcuts import render

from currency.models import Rate, ContactUs


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def contactus_list(request):
    contacts = ContactUs.objects.all()
    context = {
        'contacts': contacts
    }

    return render(request, 'contactus_list.html', context)
