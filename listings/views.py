from django.shortcuts import render, get_object_or_404
from .models import Category, Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, price_choices, state_choices
from django.contrib import messages
from inquiry.forms import InquiryForm


# Create your views here.
def index(request):

    listings = Listing.objects.filter(is_publish=True).order_by('-list_date')

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }

    return render(request, "listings/listings.html", context)

def single_listing(request, listing_id):

    single_listing = get_object_or_404(Listing, pk=listing_id)

    related = Listing.objects.filter(category=single_listing.category).exclude(id=listing_id)[:2]

    if request.method == "POST":
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
        messages.success(request, "Thank you for your email. We'll get back to you soon!")

    else:
        form = InquiryForm()

    context = {
        "single_listing": single_listing,
        "related": related,
        "form": form
    }

    return render(request, "listings/single.html", context)


def getTopic(request, name):

    cat = get_object_or_404(Category, name=name)

    post = Listing.objects.filter(category=cat.id)

    context = {
        "post": post,
        "cat": cat
    }

    return render(request, "listings/category.html", context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "queryset_list": queryset_list,
        'values': request.GET
    }

    return render(request, "listings/search.html", context)
