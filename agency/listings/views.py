from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from listings.choices import price_choices, room_choices
from .models import Listing


def index(request):
  listings = Listing.objects.order_by('-list_date')

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings,
  }

  return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  photos = [
    listing.photo_1,
    listing.photo_2,
    listing.photo_3,
    listing.photo_4,
    listing.photo_5,
    listing.photo_6,
  ]

  context = {
    'listing': listing,
    'photos': photos,
  }

  return render(request, 'listings/listing.html', context)


def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Улица
  if 'street' in request.GET:
    street = request.GET['street']
    if street:
      queryset_list = queryset_list.filter(street__iexact=street)

  # Город
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # Район
  if 'district' in request.GET:
    district = request.GET['district']
    if district:
      queryset_list = queryset_list.filter(district__iexact=district)

  # Количество комнат
  if 'rooms' in request.GET:
    rooms = request.GET['rooms']
    if rooms:
      queryset_list = queryset_list.filter(rooms_number__gte=rooms)

  # Максимальная цена
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)


  context = {
    'price_choices': price_choices,
    'room_choices': room_choices,
    'listings': queryset_list,
    'values': request.GET,
  }

  return render(request, 'listings/search.html', context)
