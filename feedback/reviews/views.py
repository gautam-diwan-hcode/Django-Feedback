from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):

    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        # if form.is_valid():
        #     form_data = form.cleaned_data
        #     review = Review(
        #         user_name=form_data['user_name'],
        #         review_text=form_data['review_text'],
        #         rating=form_data['rating'])
        #     review.save()
        #     return HttpResponseRedirect("/thank-you")

        # Model Form approach

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
