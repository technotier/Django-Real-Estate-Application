from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
        messages.success(request, "Thank you for your email. We'll get back to you soon!")

    else:
        form = ContactForm()

    context = {
        "form": form
    }

    return render(request, "contact/contacts.html", context)


