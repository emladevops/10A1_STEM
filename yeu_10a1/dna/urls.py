# dna_transformer/urls.py
from django.urls import path
from .views import transform_dna

urlpatterns = [
    path('', transform_dna, name='transform_dna'),
]

