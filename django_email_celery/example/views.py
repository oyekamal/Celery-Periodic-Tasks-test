from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from .tasks import go_to_sleep

# Create your views here.
def index(request):
    go_to_sleep.delay(10)
    # sleep(5)
    return HttpResponse("Done!!")