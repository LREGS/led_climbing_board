import requests
import asyncio 
import json

#have server working?!


def sendRouteToServer(route):
    url ="http://192.168.1.130:8090/processRoute" 

    # response = requests.post(url, json=route)
    response = requests.post(url, json=route)

def creatingRoute(hold):
    url ="http://192.168.1.130:8090/createRoute"
    response = requests.post(url, json=hold) 


# sendRouteToServer(route, url)