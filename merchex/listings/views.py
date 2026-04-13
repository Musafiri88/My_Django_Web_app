from django.shortcuts import render
from listings.models import Band


def homepage(request):
    '''View function for the homepage of the listings app.'''
    return render(request, 'listings/home.html')


def listings(request):
    '''View function for the listings page.'''
    bands = Band.objects.all()
    context = {
        'bands': bands,
    }
    return render(request, 'listings/listings.html', context)
