from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

from .choices import price_choices, bedroom_choices, state_choices
from itertools import chain


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) 
    
    paginator = Paginator(listings, 3)
    page = request.GET.get('page') 
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }


    return render(request, 'listings/listings.html', context) 

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    #queryset_list = Listing.objects.get_queryset()
    queryset_list = []
    '''
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    '''
    
    #'''
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            qs1 = Listing.objects.filter(description__icontains=keywords)
            qs2 = Listing.objects.filter(title__icontains=keywords)
            queryset_list = set(chain(qs1, qs2))
    #'''
        
    # City -- used for searching title keywords
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            q1 = Listing.objects.filter(city__icontains=city)
            if queryset_list:
                queryset_list = set(chain(queryset_list, q1))
            else:
                queryset_list = chain(q1)
            

    # Area -- previously State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            q1 = Listing.objects.filter(state__iexact=state)
            if queryset_list:
                queryset_list = set(chain(queryset_list, q1))
            else:
                queryset_list = chain(q1)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            q1 = Listing.objects.filter(bedrooms__lte=bedrooms)
            if queryset_list:
                queryset_list = set(chain(queryset_list, q1))
            else:
                queryset_list = chain(q1)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            q1 = Listing.objects.filter(price__lte=price)
            if queryset_list:
                queryset_list = set(chain(queryset_list, q1))
            else:
                queryset_list = chain(q1)
    # problem if when i only type price input i want strict results only
    # pertaining to my search ... nothing else
    # current solution -- first check if in request.GET if only price search parameters are present... else return with all the other search params included
    
    context={
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)