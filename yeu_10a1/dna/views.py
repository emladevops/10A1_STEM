# dna_transformer/views.py
from django.shortcuts import render

def transform_dna(request):
    original_text = request.POST.get('original_text', '')
    transformed_text = transform_dna_text(original_text)
    return render(request, 'index.html', {'original_text': original_text, 'transformed_text': transformed_text})

def transform_dna_text(text):
    # Replace T with A, A with T, G with X, X with G, C with G
    transformation_dict = {'T': 'A', 'A': 'T', 'G': 'X', 'X': 'G', 'C': 'G'}
    return ''.join(transformation_dict.get(char, char) for char in text)

