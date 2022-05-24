from django.urls import path

from owners.views import OwnerView, DogView

urlpatterns = [
    path("", OwnerView.as_view()),
    path("/dogs", DogView.as_view()),
]