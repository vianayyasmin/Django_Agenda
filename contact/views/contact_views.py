from django.shortcuts import render, get_list_or_404
from django.http import Http404
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True)

    context = {
        'contacts': contacts,
    }

    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id, show=True).first()

    context = {
        'contact': single_contact,
    }

    return render(request, 'contact/contact.html', context)
