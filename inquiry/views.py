# from django.shortcuts import render
# from django.contrib import messages
# from .forms import InquiryForm
#
# # Create your views here.
# def index(request):
#
#     if request.method == "POST":
#         form = InquiryForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#         messages.success(request, "Thank you for your email. We'll get back to you soon!")
#
#     else:
#         form = InquiryForm()
#
#     context = {
#         "form": form
#     }
#     return render(request, "listings/single.html", context)
