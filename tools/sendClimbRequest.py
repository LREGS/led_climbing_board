import requests
import asyncio 
import json

#have server working?!


route = {'start': '23', 'middle holds': (23,32,13,32), 'finish holds': (12,90)}


def sendRouteToServer(route):
    url ="http://192.168.1.130:8090/processRoute" 

    # response = requests.post(url, json=route)
    response = requests.post(url, json=route)

def creatingRoute(hold):
    url ="http://192.168.1.130:8090/createRoute"
    response = requests.post(url, json=hold) 


# sendRouteToServer(route, url)