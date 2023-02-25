# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, jacksonPage, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('jackson/', jacksonPage, name='jackson'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results')
]
