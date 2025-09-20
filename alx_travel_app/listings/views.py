
from django.http import JsonResponse

def index(request):
    return JsonResponse({'status': 'ok', 'app': 'listings'})

from django.shortcuts import render

# Create your views her
