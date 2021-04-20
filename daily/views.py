from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from daily.models import Article


def index(request):
    template = loader.get_template('daily/index.html')
    return render(request, 'daily/index.html')
