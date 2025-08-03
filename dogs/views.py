from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import httpx


@require_POST
def create_dog(request):
    dogsResult = httpx.get("https://dog.ceo/api/breeds/image/random")
    print(dogsResult.text)
    return HttpResponse(dogsResult.text)
