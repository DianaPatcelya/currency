from django.http.response import HttpResponse

from currency.models import Rate, ContactUs


def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type: {rate.type}, '
            f'source: {rate.source}, created: {rate.created} <br>'
        )

    return HttpResponse(str(results))


def contactus_list(request):

    results = []
    contacts = ContactUs.objects.all()

    for contact in contacts:
        results.append(
            f'ID: {contact.id}, Email: {contact.email_from}, '
            f'Subject: {contact.subject}, Message: {contact.message}'
        )

    return HttpResponse(str(results))
