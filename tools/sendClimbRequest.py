import requests
import asyncio 
import json

#have server working?!

url = "http://192.168.1.130:8090/processRoute"
route = {'start': '23', 'middle holds': (23,32,13,32), 'finish holds': (12,90)}


def sendRouteToServer(route, url):
    response = requests.post(url, json=route)
    print(response.text)


# sendRouteToServer(route, url)