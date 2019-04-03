from django.shortcuts import render
from listings.models import Category, Listing
from realtors.models import Realtor
from blog.models import Article
from listings.choices import bedroom_choices, price_choices, state_choices
from testimonials.models import Testimonial

# Create your views here.
def index(request):

    recent = Listing.objects.filter(is_publish=True).order_by('-list_date')[:4]

    featured = Listing.objects.filter(is_featured=True).order_by('-list_date')[:3]

    sale = Listing.objects.filter(sale_type=True).order_by('-list_date')[:4]

    cat_property = Category.objects.all()

    blog = Article.objects.order_by('-posted_on')[:3]

    testimonials = Testimonial.objects.all()

    context = {
        "recent": recent,
        "featured": featured,
        "sale": sale,
        "cat_property": cat_property,
        "blog": blog,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "testimonials": testimonials,
    }

    return render(request, "pages/index.html", context)

def about(request):

    realtor = Realtor.objects.all()

    testimonials = Testimonial.objects.all()

    context = {
        "realtor": realtor,
        "testimonials": testimonials,
    }

    return render(request, "pages/about.html", context)

