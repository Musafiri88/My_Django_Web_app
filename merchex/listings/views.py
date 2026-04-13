from django.shortcuts import render


def homepage(request):
    '''View function for the homepage of the listings app.'''
    return render(request, 'listings/home.html')
