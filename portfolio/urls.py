from django.urls import path

from portfolio.views import Landingpage

urlpatterns = [
    path('', Landingpage.as_view()),
]