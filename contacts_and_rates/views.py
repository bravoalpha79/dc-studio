from django.shortcuts import render
from .models import ContactInfo, RateList, RateLink


def contacts(request):
    contact_info = ContactInfo.objects.all().order_by('-updated_at').first()

    return render(request, "contacts_and_rates/contacts.html", {"contact_info": contact_info})


def rates(request):
    ratelist = RateList.objects.all().order_by('-updated_at').first()
    ratelink = RateLink.load()

    context = {"ratelist": ratelist, "ratelink": ratelink}

    return render(
        request, "contacts_and_rates/rates.html", context
    )
