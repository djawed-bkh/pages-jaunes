from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from entreprises.models import Entreprise
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def home(request):
    return render(request,'base.html')