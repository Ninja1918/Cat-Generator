from django.shortcuts import render, redirect
from django.views import View
import requests
import urllib.parse
import time

class home(View):
    cat_api = "https://api.thecatapi.com/v1/images/search"
    url = cat_api
    def get(self, request):
        response = []
        for i in range(10):
            response.append(requests.get(self.url).json())
            time.sleep(0.200)
        print(response)
        return render(request, 'homePage/home.html', {"res" : response})