from django.shortcuts import render, redirect
from django.views import View
import requests
import urllib.parse
import time

class home(View):
    nsfw = False
    waifu_api = "https://api.waifu.im/random?"
    url = waifu_api + urllib.parse.urlencode({"is_nsfw" : nsfw})
    def get(self, request):
        # resp = requests.get("https://api.waifu.im/random", params = parameters).json()
        response = []
        for i in range(10):
            response.append(requests.get(self.url).json()["images"])
            time.sleep(0.200)
        return render(request, 'homePage/home.html', {"res" : response, "nsfw": self.nsfw})
    def post(self, request):
        return redirect('nsfw')

class nsfw(View):
    nsfw = True
    waifu_api = "https://api.waifu.im/random?"
    url = waifu_api + urllib.parse.urlencode({"is_nsfw" : nsfw})
    def get(self, request):
        # resp = requests.get("https://api.waifu.im/random", params = parameters).json()
        response = []
        for i in range(10):
            response.append(requests.get(self.url).json()["images"])
            time.sleep(0.200)
        return render(request, 'homePage/home.html', {"res" : response, "nsfw": self.nsfw})
    def post(self, request):
        return redirect('home')